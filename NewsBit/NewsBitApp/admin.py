from django.contrib import admin
from .models import news,Author,Comment,Category
# Register your models here.

admin.site.register(news)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
# admin.site.register(Tag)
