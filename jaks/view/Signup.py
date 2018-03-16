from django.shortcuts import render
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
        return render(request, 'signup.html')

    def post(self,request):
        user_name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        dob = datetime.datetime.now().date()
        res = sql_service.save_user_data(user_name,email,password,dob,gender)
        if res:
            data = {"flag":True,"id":res}
        else:
            data = {"flag":False,"msg":"ERROR,Save Again!!!"}
        return HttpResponse(json.dumps(data))


class SavePackage(View):
    def post(self,request):
        user= request["user_id"]
        package_name = request["package_name"]
        user = User.objects.get(id=user)
        package_name= "Free"
        package_id = sql_service.get_package_id(package_name)
        print(package_id,"=============")
        sql_service.save_user_package(package_id,user)

        total_limits=0
        limit_used =0
        left_limit = 0
        api_key = str(hexlify(os.urandom(16)))
        sql_service.save_buying_history(user,total_limits,limit_used,left_limit,api_key)
        return HttpResponse(True)

