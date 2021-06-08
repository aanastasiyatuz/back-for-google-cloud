from django.contrib.auth import get_user_model
from django.db import models


MyUser = get_user_model()

class ProfileProvider(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='provider')
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='providers', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, primary_key=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.slug = self.user.email.split('@')[0]
        super().save(*args, **kwargs)

class ProfileClient(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='client')
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='clients', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, primary_key=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.slug = self.user.email.split('@')[0]
        super().save(*args, **kwargs)