from django.shortcuts import render
import random,string
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views.generic import View
from jaks.services import sql_service
import datetime
import os
from binascii import hexlify
from django.contrib.auth.models import User
import json

class Signup(View):
    def get(self,request):
        return render(request, 'signup/signup.html')

    def post(self,request):
        user_name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        dob = request.POST["dob"]
        gender_data = request.POST["gender"]
        if gender_data == 'Male':
            gender=0
        else:
            gender=1
        dob = datetime.datetime.now().date()
        res = sql_service.save_user_data(user_name,email,password,dob,gender)
        if res:
            data = {"flag":True,"id":res.id}
        else:
            data = {"flag":False,"msg":"ERROR,Save Again!!!"}
        # print(data)
        return HttpResponse(json.dumps(data))


class SavePackage(View):
    def post(self,request):
        user = request.POST["generated-id"]
        package_name = request.POST["selected-package"]
        print(package_name,11111111)
        user= User.objects.get(id=user)
        print(user,2222222222)
        package_id = sql_service.get_package_id(str(package_name).lower())
        sql_service.save_user_package(package_id,user)
        total_limits=package_id.limit
        api_key = self.random_string_generator()
        sql_service.save_buying_history(user,total_limits,api_key)
        return HttpResponse(json.dumps({"key":api_key}))


    def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(16))


class ApiGenerator(View):
    def get(self,request):
        # print(key,"=====")
        # print('xcgj,.'
        key = request.GET['key']
        return render(request, "signup/api_generator.html", {"data":key})
