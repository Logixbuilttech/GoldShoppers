from django import views
from django.urls import path,include
from .views import *


urlpatterns = [
    path('Users/', Users_list, name="users"),
    path('Company_Information/', Company_Information_list, name="company_information"),
    path('Vendors/', Vendors_list, name="vendors"),
]