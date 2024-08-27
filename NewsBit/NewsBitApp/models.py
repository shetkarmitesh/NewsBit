from django.db import models
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
    
class news (models.Model):
    img = models.ImageField(upload_to='pics')
    headline = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
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
