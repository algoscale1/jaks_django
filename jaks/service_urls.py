from django.conf.urls import include, url
from django.contrib import admin
from .view import index,Signup,LoginLogout,UserIndex
# from django.conf import settings
# from django.conf.urls.static import static
from jaks.view.classify import TextClassifier
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^subject/index',index.Index.as_view()),
    url(r'^subject/signup',Signup.Signup.as_view()),
    url(r'^subject/login', LoginLogout.Login.as_view()),
    url(r'^subject/logout', login_required(LoginLogout.Logout.as_view()),name='logout'),
    url(r'^subject/userIndex', UserIndex.UserIndex.as_view()),
    url(r'^subject/save_userdata',Signup.Signup.as_view()),
    url(r'^subject/save_package',Signup.SavePackage.as_view()),
    url(r'^subject/api_generator/$',Signup.ApiGenerator.as_view()),
    # url(r'^classify/(?P<api_key>\w{16})/$',TextClassifier.as_view(),name='classi'),
    url(r'^subject/classify/$',TextClassifier.as_view(),name='classi')
]
