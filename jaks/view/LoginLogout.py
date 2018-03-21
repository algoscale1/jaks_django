from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

class Login(View):
    def get(self,request):
        return render(request, 'login/login.html')

    def post(self,request):
        print("Login code would be here")


class Logout(View):
    def get(self,request):
        logout(request)
        request.session.flush()
        return HttpResponseRedirect('login')

