from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


# class users_role(models.Model):
#     role = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.role)

# Create your models here.


# class Users(AbstractUser):

#     username = models.CharField(
#         max_length=50, blank=True, null=True, unique=True)
#     email = models.EmailField(_("email address"), unique=True)
#     phone_number = models.CharField(max_length=10, null=True, blank=True)
#     role = models.ForeignKey(users_role, on_delete=models.CASCADE, null=True)
#     description = models.CharField(max_length=1000, null=True, blank=True)
#     is_staff = models.BooleanField()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return str(self.username) or str(self.email)


class Company_Information(models.Model):

    company_name = models.CharField(max_length=1000)
    brand_name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    tax_id = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.company_name)


class Vendors(models.Model):
    # username = models.CharField(max_length=1000)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.ForeignKey(
        Company_Information, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
    # permission = PermissionError

    def __str__(self):
        return str(self.company_name)+" - "+str(self.username)
