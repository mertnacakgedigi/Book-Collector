from django.contrib import admin
# import your models here
from .models import Book,Rating,Reader

# Register your models here
admin.site.register(Book)

admin.site.register(Rating)

admin.site.register(Reader)