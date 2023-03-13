from rest_framework import serializers
from .models import *

# class UsersSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['username', 'email', 'phone_number', 'role', 'description',]


# class users_roleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = users_role
#         fields = ['role']


class Company_InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Company_Information
        fields = "__all__"


class VendorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = "__all__"
