from django.conf.urls import include, url
from django.contrib import admin
from .view import index,Signup,Login
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^index',index.Index.as_view()),
    url(r'^signup',Signup.Signup.as_view()),
    url(r'^login', Login.Login.as_view()),
    url(r'^save_userdata',Signup.Signup.as_view())
]
