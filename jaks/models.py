from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    gender = models.IntegerField()
    date_of_birth = models.DateField()

class Package(models.Model):
    name = models.CharField(max_length=50,unique=True)
    limit = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    validity_in_months = models.IntegerField(default=0)

class UserPackage(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    pacakage = models.ForeignKey(Package,on_delete=models.PROTECT)
    package_get_date = models.DateField()
    package_end_date = models.DateField()
    status = models.IntegerField()


class BuyingHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    total_limits = models.IntegerField()
    limit_used = models.IntegerField()
    left_active_limit = models.IntegerField()
    api_key = models.CharField(max_length=50)


