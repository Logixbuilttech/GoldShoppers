from django import views
from django.urls import path,include
from .views import *


urlpatterns = [
    path('Users/', Users_list, name="users"),
    path('Users/', Users_details, name="Users_details"),
    path('Company_Information/', Company_Information_list, name="company_information"),
    path('Company_Information/', Company_Information_details, name="Company_Information_details"),
    path('Vendors/', Vendors_list, name="vendors"),
    path('Vendors/', Vendors_details, name="Vendors_details"),
]