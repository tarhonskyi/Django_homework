from django.contrib import admin
from . import models

admin.site.register(models.Actor)
admin.site.register(models.Film)

admin.site.register(models.PublishingHouse)
admin.site.register(models.Book)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'second_name', 'surname', 'birth_date', 'country']


admin.site.register(models.Author, AuthorAdmin)


class BookInStoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'book',  'quantity', 'language', 'publishing_house', 'add_to_store_date', ]
    list_filter = ['language', 'publishing_house', 'add_to_store_date']


admin.site.register(models.BookInStore, BookInStoreAdmin)
