from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from app.models import *

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, description, role, contact_no, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            description=description,
            role=role,
            contact_no=contact_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, description, role, contact_no, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            description=description,
            role=role,
            contact_no=contact_no,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model


class User_data(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    Roles = [
        ("manager", "manager"),
        ("account", "account"),
        ("billing", "billing"),
        ("sales", "sales"),
        ("custom", "custom"),
    ]
    role = models.CharField(max_length=7, choices=Roles)
    contact_no = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'description', 'role', 'contact_no']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
