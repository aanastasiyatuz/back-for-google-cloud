from django.contrib import admin
from .models import Place, Lodging, Catering,\
                    ImagePlace, ImageLodging, ImageCatering,\
                    CommentPlace, CommentLodging, CommentCatering



'''--------------------------PLACE---------------------------------'''
class ImagePlaceInlineAdmin(admin.TabularInline):
    model = ImagePlace
    fields = ('image',)
    max_num = 5

class CommentPlaceInlineAdmin(admin.TabularInline):
    model = CommentPlace
    fields = ('body', 'author')
    max_num = 10

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagePlaceInlineAdmin, CommentPlaceInlineAdmin]



'''--------------------------Lodging---------------------------------'''
class ImageLodgingInlineAdmin(admin.TabularInline):
    model = ImageLodging
    fields = ('image',)
    max_num = 5

class CommentLodgingInlineAdmin(admin.TabularInline):
    model = CommentLodging
    fields = ('body', 'author')
    max_num = 10

@admin.register(Lodging)
class LodgingAdmin(admin.ModelAdmin):
    inlines = [ImageLodgingInlineAdmin, CommentLodgingInlineAdmin]




'''--------------------------CATERING---------------------------------'''
class ImageCateringInlineAdmin(admin.TabularInline):
    model = ImageCatering
    fields = ('image',)
    max_num = 5

class CommentCateringInlineAdmin(admin.TabularInline):
    model = CommentCatering
    fields = ('body', 'author')
    max_num = 10

@admin.register(Catering)
class CateringAdmin(admin.ModelAdmin):
    inlines = [ImageCateringInlineAdmin, CommentCateringInlineAdmin]
