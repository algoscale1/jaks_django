from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.urls import reverse

class UserIndex(View):
    # def get(self,request):
    #     return render(request, 'user/index.html')

    def post(self, request):
        print("HEREEEEE",request)
        username = request.POST['user_name']
        password = request.POST['password']

        request.session.set_test_cookie()
        if not request.session.test_cookie_worked():
            return HttpResponse("Please enable cookies and try again.")
        request.session.delete_test_cookie()

        user = authenticate(username=username, password=password)
        print(user,"/****************************")

        if user is not None and User.objects.get(id=user.id).is_active:
            login(request, user)
            return render(request, 'user/index.html')
        else:
            return render(request, 'login/login.html')


