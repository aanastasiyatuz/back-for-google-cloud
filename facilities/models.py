from django.db import models
from django.contrib.auth import get_user_model

MyUser= get_user_model()

class Place(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100, blank=True, null=True)
    main_image = models.ImageField(upload_to='main_place')
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Lodging(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100, blank=True, null=True)
    main_image = models.ImageField(upload_to='main_lodging')
    average_check = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name

class Catering(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100, blank=True, null=True)
    main_image = models.ImageField(upload_to='main_catering')
    average_check = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name

'''----------IMAGES-----------'''
class ImagePlace(models.Model):
    place = models.ForeignKey('Place', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='place')

class ImageLodging(models.Model):
    lodging = models.ForeignKey('Lodging', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lodging')

class ImageCatering(models.Model):
    catering = models.ForeignKey('Catering', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='catering')

'''----------COMMENTS----------'''
class CommentPlace(models.Model):
    place = models.ForeignKey('Place', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='place')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.body[:20]}'

class CommentLodging(models.Model):
    lodging = models.ForeignKey('Lodging', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='lodging')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.body[:20]}'

class CommentCatering(models.Model):
    catering = models.ForeignKey('Catering', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='catering')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.body[:20]}'

