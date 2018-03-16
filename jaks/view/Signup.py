from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views.generic import View
from jaks.services import sql_service
import datetime


class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        user_name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        dob = datetime.datetime.now().date()
        gender = 1
        sql_service.save_user_data(user_name,email,password,dob,gender)
        return HttpResponse(True)


