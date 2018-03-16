from django.contrib.auth.models import User
from jaks.models import UserProfile,Package,UserPackage,BuyingHistory
import datetime
from django.core.exceptions import ObjectDoesNotExist

def save_user_data(user_name,email,password,dob,gender):
    try:
        user = User(username=user_name,email=email,password=password)
        user.save()
        # user = User.objects.get(id=1)
        print(user, 'kkkkk')
        print(dob,gender)
        UserProfile(user=user,date_of_birth=dob,gender=gender).save()
        print('Done')
        return user
    except Exception as e:
        return False

def get_package_id(package_name):
    package = Package.objects.get(name=package_name)
    return package

def save_user_package(package_id,user_id):
    print("SAVING USER PACKAGE")
    package_get_date = datetime.datetime.now().date()
    package_end_date = datetime.datetime.now().date()
    status = 1
    UserPackage(user=user_id,pacakage=package_id,package_get_date=package_get_date,
                package_end_date=package_end_date,status=status).save()
    print("DONEEEE")



def save_buying_history(user,total_limits,limit_used,left_limit,api_key):
    print("SAVING BUYING HISTORY")
    BuyingHistory(user=user,total_limits=total_limits,limit_used=limit_used,left_active_limit=left_limit,api_key=api_key).save()
    print("Donee22222")


def check_api_key_validity(key):
    """

    :param key:
    :return:
    """
    try:
        ff = BuyingHistory.objects.get(api_key=key)
        if ff.limit_used ==ff.total_limits:
            return "False"
        ff.limit_used += 1
        ff.save()
    except ObjectDoesNotExist:
        return "False"

    return "True"


def increase_hit_count(key):
    """

    :param key:
    :return:
    """

