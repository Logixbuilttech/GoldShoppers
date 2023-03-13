import imp
from django.contrib import admin
from django.urls import path, include
from user_auth.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', csrf_exempt(UserLogin.as_view()), name='login'),
    # path('mapdetails/', MapDetails.as_view(), name='mapdetails'),
    path('userprofile/',  csrf_exempt(UserProfileView.as_view()), name='userprofile'),
    # path('changepassword/', UserChangePassword.as_view(), name='changepassword'),
    # path('send-reset-password-email/', SendPasswordResetEmail.as_view(),
    #  name='send-reset-password-email'),
    # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),
    #  name='reset-password/'),
]



