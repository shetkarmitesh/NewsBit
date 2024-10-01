from django.db import models
# from django.contrib.auth.models import User,auth
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# about one onject
from django.db import IntegrityError


from django.contrib.humanize.templatetags import humanize
# from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# taggit for tags
# from taggit.managers import TaggableManager



class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='user_profile')

    phoneNo = models.IntegerField(null=True)
    birth_date=models.DateField(null=True)


class Category(models.Model):
           
    color_choices = {
    "danger": "danger",
    "primary": "primary",
    "success": "success",
    "info": "info",
    "warning": "warning",
    "light": "light",
    "dark": "dark",
    "transparent": "transparent",
    }
    name = models.CharField(max_length=50,unique=True)
    name_color = models.CharField(max_length=50,choices=color_choices,default="primary")

    def __str__(self):
        return f'{self.id} {self.name}' 

class Tag(models.Model):
    class tagType(models.TextChoices):
        Tech = "Tech"
    color_choices = {
    "danger": "danger",
    "primary": "primary",
    "success": "success",
    "info": "info",
    "warning": "warning",
    "light": "light",
    "dark": "dark",
    "transparent": "transparent",
    }
    tag = models.CharField(max_length=100)
    # name = models.CharField(max_length=50,choices=tagType.choices,default=tagType.Tech,unique=True)
    # name_color = models.CharField(max_length=50,choices=color_choices,default="primary")
    # tag = models.ManyToManyField(Category)
    def __str__(self):
        return f'{self.id} {self.tag}' 



class Author(models.Model):
    img = models.ImageField(upload_to='author')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    description1 = RichTextUploadingField(null=True,blank=True)

    def post_count(self):
        count = news.author_post(self)  
        return count
  
    
    def author_name(self):
        return self.first_name +" "+self.last_name
    def __str__(self) :
        return f'{self.first_name + " "+self.last_name}'

class news (models.Model):
    img = models.ImageField(upload_to='pics')
    headline = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=1)
    # tags = models.CharField(max_length=100)
    # jugad
    # tagBackColor = models.CharField(max_length=100)

    # This option sets the field to the current datetime when the object is first created and does not update it afterwards.
    datetime = models.DateTimeField(auto_now_add=True)
    # description = CKEditor5Field(null=True,blank=True,config_name='extends')
    # description1 = RichTextField(null=True,blank=True)
    description1 = RichTextUploadingField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    editor_choice= models.BooleanField()
    
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

    def category_name(self):
        return self.category.name
    def category_color(self):
        return self.category.name_color
    
    def author_post(self):
        count = news.objects.all().filter(author_id = self.id)
        return len(count)
    def comments_count(self):
        return Comment.comment_count(self)

    def __str__(self) :
        return f'{self.id} {self.headline}'
    
class Comment(models.Model):
    post = models.ForeignKey('news', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name="parent_id")
    sub_parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name="sub_parent_id")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="user")
    def __str__(self):
        return f" {self.id} Comment by {self.user.first_name}{self.user.last_name} on {self.post}"

    # want to display user commented img for now just author img
    def author_img(self): 
        return self.author.img
    def author_name(self):
        return self.author.first_name+" "+self.author.last_name
    def get_time(self):
        return humanize.naturaltime(self.created_at)

    def comment_count(self):
        comments = Comment.objects.all().filter(post_id=self.id)

        return len(comments)

class aboutDetails(models.Model):

    history = RichTextUploadingField(null=True,blank=True)
    mission = RichTextUploadingField(null=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.pk and aboutDetails.objects.exists():
            raise IntegrityError(
                "There can be only one about you can not add another"
            )
            return None
        return super(aboutDetails, self).save(*args, **kwargs)

class Team_members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='teams')
    def name(self):
        return self.first_name +" "+self.last_name