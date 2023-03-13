from urllib import request
from django.contrib import admin
from . models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin

# admin.site.register(Jobseeker)
# admin.site.register(Users)
admin.site.register(Vendors)
admin.site.register(users_role)
admin.site.register(Company_Information)
# Register your models here.

# @admin.register(Vendors)
# class VendorAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     def get_form(self,request,obj=None,**kwargs):
#         is_superuser = request.user.is_superuser

#     if not is_superuser:


class CustomeUserAdmin(UserAdmin):
    model = Users
    form = CustomUserChangeForm
    add_from = CustomUserCreationForm

    fieldsets = (
        # *UserAdmin.fieldsets,
        (None, {"fields": ("username","email",'phone_number',"first_name","last_name",'role',"is_staff", "is_active", "is_superuser", "groups"
                           )}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","email","first_name","last_name", "phone_number",'role' , "password1", "password2", "is_staff",
                "is_active", "groups" 
            )}
        ),
    )



admin.site.register(Users,CustomeUserAdmin)