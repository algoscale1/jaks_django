from django.contrib.auth.models import User
from jaks.models import UserProfile


def save_user_data(user_name,email,password,dob,gender):
    try:
        user = User(username=user_name,email=email,password=password).save()
        # user = User.objects.get(id=1)
        print(user)
        print(dob,gender)
        UserProfile(user=user,date_of_birth=dob,gender=gender).save()
    except Exception as e:
        print(e,"+++++++++++++++++=")