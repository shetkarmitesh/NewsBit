from django.contrib import admin
from .models import news,Author,Comment,Category
# Register your models here.

# class newsAdmin(admin.ModelAdmin) :
#     def __init__ (self):
#         pass

admin.site.register(news)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
# admin.site.register(Tag)
