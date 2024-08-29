from django.db import models
from django.contrib.auth.models import User,auth

from django.contrib.humanize.templatetags import humanize
# from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# class Tags(models.Model):
#     class tagType (models.TextChoices):
#         Entertainment = 'Entertainment'
#         Game = 'Game'
#         Travel = 'Travel'
#         LifeStyle = 'LifeStyle'
#         Tech = 'Tech'
#         Tour = 'Tour'
#         Health = 'Health'
#         Google = 'Google'
#         Fashion = 'Fashion'
        
#         Eyes = 'Eyes'
#         Hair = 'Hair'
#         Nail = 'Nail'
#         Lips = 'Lips'
#     tag = models.CharField(max_length=100)

#     @classmethod
#     def tag(self):
#         return [(key.value) for key in self]
    
class Author(models.Model):
    img = models.ImageField(upload_to='author')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    description1 = RichTextUploadingField(null=True,blank=True)

class news (models.Model):
    img = models.ImageField(upload_to='pics')
    headline = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=1)
    tags = models.CharField(max_length=100)
    # jugad
    tagBackColor = models.CharField(max_length=100)
    # This option sets the field to the current datetime when the object is first created and does not update it afterwards.
    datetime = models.DateTimeField(auto_now_add=True)
    # description = CKEditor5Field(null=True,blank=True,config_name='extends')
    # description1 = RichTextField(null=True,blank=True)
    description1 = RichTextUploadingField(null=True,blank=True)

    def get_time(self):
        return humanize.naturaltime(self.datetime)

    def author_name(self):
        return self.author.first_name +" "+self.author.last_name
    # def author_lname(self):
    #     return self.author.last_name
    def author_desc(self):
        return self.author.description
    def author_img(self):
        return self.author.img


class Comment(models.Model):
    post = models.ForeignKey('news', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    # want to display user commented img for now just author img
    def author_img(self): 
        return self.author.img
    def author_name(self):
        return self.author.first_name+" "+self.author.last_name
    def get_time(self):
        return humanize.naturaltime(self.created_at)
    