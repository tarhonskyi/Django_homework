from django.contrib import admin
from . import models

admin.site.register(models.Actor)
admin.site.register(models.Film)
admin.site.register(models.Author)
admin.site.register(models.PublishingHouse)
admin.site.register(models.Book)


class BookInStoreAdmin(admin.ModelAdmin):
    list_display = ['book', 'language', 'publishing_house', 'quantity',]


admin.site.register(models.BookInStore, BookInStoreAdmin)
