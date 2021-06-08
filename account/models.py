from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

STATUS_CHOICES = (
    ('provider', 'provider'),
    ('client', 'client'),
)

class MyUser(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=False, blank=False, unique=True)
    status = models.CharField(default='client', max_length=20, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
