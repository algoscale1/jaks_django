from django.conf.urls import include, url
from django.contrib import admin
from .view import index,Signup,Login,UserIndex
# from django.conf import settings
# from django.conf.urls.static import static
from jaks.view.classify import TextClassifier

urlpatterns = [
    url(r'^index',index.Index.as_view()),
    url(r'^signup',Signup.Signup.as_view()),
    url(r'^login', Login.Login.as_view()),
    url(r'^userIndex', UserIndex.UserIndex.as_view()),
    url(r'^save_userdata',Signup.Signup.as_view()),
    url(r'^save_package',Signup.SavePackage.as_view()),
    url(r'^api_generator/$',Signup.ApiGenerator.as_view()),
    url(r'^classify',TextClassifier.as_view(),name='classi')
]
