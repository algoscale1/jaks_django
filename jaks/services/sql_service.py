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
    #Package(name="free",cost=0,limit=60,validity_in_months=6).save()
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



def save_buying_history(user,total_limits,api_key):
    print("SAVING BUYING HISTORY")
    BuyingHistory(user=user,total_limits=total_limits,api_key=api_key).save()
    print("Donee22222")

def get_api_key(user_id):
    user = User.objects.get(id=user_id)
    BuyingHistory.objets.get(user = user,total_limits__gt = 0)


def check_api_key_validity(key):
    """

    :param key:
    :return:
    """
    try:
        print("hereeeeeeeeeeeeeeeeee")
        ff = BuyingHistory.objects.get(api_key=key)
        if ff.total_limits == 0:
            return "False"
        ff.total_limits = ff.total_limits-1
        ff.save()
    except ObjectDoesNotExist:
        return "False"

    return "True"


def increase_hit_count(key):
    """

    :param key:
    :return:
    """

