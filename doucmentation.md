
  we are  creating virtual environment for this project so we can isolate python installs , and pip packages and also used to manage packages allow developers to control software dependencies in Python code.

  Install virtual environment using : pip install virtualenvwrapper-win

  creating virtual environment : python -m venv myenv

  activating the virtaul environment : .\myenv\Scripts\activate

  We are done with our virtaul environment now we have to setup django

  instll django : pip install Django

  creating project  : django-admin startproject NewsBit 
 project has been created move to the project : cd NewsBit

 lets test the project is running or not using : python manage.py runserver

 creating app : python manage.py startapp NewsBitApp

 we have to mapped the urls in app for that we have to create the urls.py

 In urls.py file we haved define the home page as index.html 
 the we have to define the index function in views to render or display message 

 but if we want to go home page we have to define in project urls also about the new app furniapp :  path('', include ("NewsBitApp.urls")), 
 for that we have imported include along with path

 and the website is rendering to the index page but it is not rendering because we haved to define in settings.py file the template directory
'DIRS': [os.path.join(BASE_DIR,'templates')],

 now we have to link the css and other static files 
 
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'assets')

now create folder static and paste all folder like css js

run command to : python manage.py collectstatic

now we are ready with the css, js other static files but it doesnt affect the index.files because we have to make all the links static in index.html  using jinja format
1. {% load static %}
2. make the all the links static by : href="{% static 'favicon.png'%} "

we are able to see the changes and mapped all the links

for images : 
        for img we should define : {% static "img/place" as baseUrl %}
        static and path as baseUrl as variable
        <img src="{{ baseUrl }}/{{ dest.img }}" alt="asfasdfasdfadf">

mapped all the links as the static in each files 

*****error*****
in this project we have included all the neccessary files using include statement : {% include 'partials/header.htm' %} 
in main index.html we haved included the header and footer using include statement

 during the logo  
 <img src="{% static 'images/logos/logo.png'%}" alt="logo"> we haved replaced the link with static 

 features slider images were no accessible so from the below link we found the solution 
https://simpleit.rocks/python/django/call-static-templatetag-for-background-image-in-css/

******** mysql database register ***********

Lets define the database 
In settings.py file database secttion :

        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'furnitureDetails',
        'USER': 'root',
        'PASSWORD': 'zxcvbnm1234567890$',
        'HOST':'localhost',
        'PORT':'3306' 
            }
 
and download MySQLclient : pip install mysqlclient
we have to declare our application name in settings.py : 
       # defnine app
    'NewsBitApp.apps.NewsbitappConfig',

created meet with an error like cannot use ImageFeild because Pillow is not installed
    pip install Pillow

************ Register Login Logout ***************
make action Register/login/logout , method as port mapped the urls 
fetch details about user and requested user match the data and process the next step such as register , login ,logout


****************News Model *************
It is model which contain info about the news like headline , tags , description, images, etc

passed the data to the index page 

*************** Single Post ******************
we are required to display the content in proper format as required for that we are using the ckeditor which provide such functionalties 
Ckeditor is  rich text editor which enables writing content directly inside of web pages or online applications.

-----------ckeditor setup -------------
 Install and Set Up CKEditor : pip install django-ckeditor

Add ckeditor and ckeditor_uploader to your INSTALLED_APPS in settings.py:
      INSTALLED_APPS = [
    ...
    'ckeditor',
    'ckeditor_uploader',
    ...
    ]
  
  Add CKEditor settings to settings.py:
  CKEDITOR_UPLOAD_PATH = "uploads/"

Include CKEditor URLs in your urls.py:
    urlpatterns = [
        ...
        path('ckeditor/', include('ckeditor_uploader.urls')),
        ...
    ]



adding more functionalities 

# # # ck editor 5 custom paltet config
customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]
# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
CKEDITOR_CONFIGS  = {
    # 'default': {
    #     'toolbar': ['heading', '|', 'bold', 'italic', 'link',
    #                 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    # }
    'default': {
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule',],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList'],
            ['Indent','Outdent'],
            ['Maximize'],
        ],
        'extraPlugins': 'justify,liststyle,indent','toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            
        ]),
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft', 
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

in model: 
import from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
    
object : description1 = RichTextUploadingField(null=True,blank=True)

In templates to display the {{news.description1|safe}}  

got from the stackoverflow

now we are ablle to create the dynamic contain as per required


------------- Time Ago -------------
our article requires the timeline like 2 hours ago etc for that we have inbuild methods we just have to mention in files 
in settings.py : 
    INSTALLED_APPS = [
        'django.contrib.humanize',
    ]

To store the current indian time we change the zone as asian/kolkata
DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NewsBitDatabase',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'localhost',
        'PORT':'3306' ,
        'TIME_ZONE': 'Asia/Kolkata'
            }
}

now in models we create the funtion get_time which provide naturaltime 
from django.contrib.humanize.templatetags import humanize
in class
    datetime = models.DateTimeField(auto_now_add=True)

    def get_time(self):
            return humanize.naturaltime(self.datetime)



****************** Author model *******************
class Author(models.Model):
    img = models.ImageField(upload_to='author')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    description1 = RichTextUploadingField(null=True,blank=True)

now we faced the error while sending the author id to show the data 
auhtor id is sending from two different place like from news single post and from specific author using id 

that error is handled by using if statement in jinja :
            {% if author_detail is not none %}
                href="{% url 'author' author_detail.id  %}"
            {%else%}
                href="{% url 'author' news.author.id  %}"  
            {% endif%} 


*************** Comments *********************
created model for comment 

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

parent_comment is most important for mapping the comments serially 

logic for arranging the comments in form we first extract parent comments then parent comments subcomment and order by parent_comment id 
 parentComments = Comment.objects.all().filter(post_id = new.id,parent_comment_id=None)
    subComments = Comment.objects.all().filter(post_id = new.id).filter(~Q(parent_comment_id=None)).order_by('parent_comment_id')
    

facing the the error while posting comment 
link which is forming : http://127.0.0.1:8000/single-post/2/postComment
error :  
^(?P<path>.*)$
The current path, single-post/2/postComment, matched the last one.
Page not found (404)
“P:\WorkSpace\Django\Projects\NewsBitProject\NewsBit\media\single-post\2\postComment” does not exist
 where form is :  <form action="postComment" method="post">

view function for postComment:
def postComment(request):
    if request.method =="POST":

        print("hhii")
        return redirect('/')

    return render(request,"single-post.html")



    
we resolve the error by adding the / in form action : <form action="/postComment" method="post">
 now we hitting the postComment successfully : 


we are posting the comment without parent comment id  now lets create the logic for replying to parent comment for that we have to click reply Button
after servral try i got 2 way to solve posting commnet 
 error while activating all reply buttons for all comments 
 first way :
    in reply button we call an js function and comment id as parameter and get second div id  with comment id 

<a class="comment-reply" onclick=comment({{comment.id}})></i> Reply</a>
<div id="secondDiv{{comment.id}}">
This is my DIV element.
</div>
function comment({{comment.id}}) {
        var secondDiv = document.getElementById("secondDiv{{comment.id}}");
        if (secondDiv.style.display === "none") {
            secondDiv.style.display = "block";
        } else {
            secondDiv.style.display = "none";
        }
    };

second way : 
i found about collapse in bootstrap i used that 

<a class="comment-reply" data-toggle="collapse" data-target="#collapseExample{{comment.id}}" aria-expanded="false" aria-controls="collapseExample{{comment.id}}" ><i class="fa fa-reply"></i> Reply</a>
                        
                        <div class="collapse" id="collapseExample{{comment.id}}">
                            <div class="card card-body">
                                <form action="/postComment" method="post">
                                    {% csrf_token %}
                                    <input type="hidden" name="news_id" value="{{news.id}}" id="comment_id">
                                    <input type="hidden" name="author_id" value="{{news.author_id}}" id="comment_id">
                                    <input type="hidden" name="parentComment_id" value="{{comment.id}}" id="comment_id">
                                    <div class="form-group">
                                        <label for="comment">Post a reply </label>
                                        <input type="text" class="form-control" name="content" placeholder="Enter comment here">
                                        <button type="submit" class="btn btn-light">Submit</button>
                                    </div>
                                </form>
                            </div>
                        </div>


now its works fine 

but we new issue that is we only have parent comment and its child comments but if any reply to child comments is doesnt display
we are lagging in the displaying the comments properly


******************** category model ******************
category is a model which conatain type such as health , game , tech , entertainment,etc
for that we have declare an category type inside the category model with text choices 
class CategoryType(models.TextChoices):
        Entertainment = 'Entertainment'
        Game = 'Game'
    name = models.CharField(max_length=50,choices=CategoryType.choices)

now we have to add category color to display with color lke primary, info , danger 

above logic is not suitable for new category type so we have decalre normal varible with unique and assign color with choices

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

lets comment tags and tag color in news model
    tags = models.CharField(max_length=100)
    # tagBackColor = models.CharField(max_length=100)


now we reuired tags which contain multiple category for that we are using many to many field 
#     # tag = models.ManyToManyField(Category)
it run successfully for experimental model tags : 

but while adding it in news feild we get error as : 
Explanation: This error occurs when two or more relationships in your Django models use the same default reverse accessor name. In your case, it seems that both category and tags fields are trying to use the same default reverse accessor name.

solution we found that is assign the related name to each fields that uses ForeignKeyor many many feild 
category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='news_by_category')
    tags = models.ManyToManyField(Category, related_name='news_by_tags')

now lets access the tags in post  for that we have to fetch all the objects of tags as : news.tags.all
now iterate it 
        {%for item in news.tags.all%}
        <a href="{% url 'post-category-2'%}">{{item.name}}</a>
        {%endfor%}
item.name is from category model



*************** post-category ************



creating page to display data for specific category like life style,game ,tech
page requesting gor post-category-1.html here we need to pass category id instead of 1 and have to maintain only one html page

passed the tag id  like 

{%for item in news.tags.all%}
                <a href="{% url 'post-category' item.id %}"> {{item.name}}</a>
                
{%endfor%}

mapped the urls as  :path('post-category/<int:category_id>', views.post_category,name="post-category"),
now the view function 

def post_category(request,category_id):
    news_details = news.objects.all().filter(tags = category_id)
    print(len(news_details))
    return render(request,'post-category-2.html',{'news':news_details})

to access the id of tag for fetching specific news post applay filter :  filter(tags = category_id)

post-category contain one include statement of breadcrum which one argument with in for that we are using with statement to pass the argument 

as {% include "partials/blocks/breadcrumb.htm" with title="asdf" %} 
where we faced the error to pass the argument error was the space between title and = like  title="asdf"
error : 
        TemplateSyntaxError at /post-category/2
        "with" in 'include' tag needs at least one keyword argument.
solve error because of : Looks like Django is quite picky about whitespace in this instance

now to acccess that title just use {{title}} it will print the value in it

it is beneficial because in wont accept the value from the database or view function so we have directly add the values like {{titles}}
                    <li>{{title}}</li>
in breadcrum.htm and post-category-2.html title section 

now from here we are including the post-six-style which have multiple news and slidebar 
so here we have achieve pagination later ********************************************************



**************editor choices ****************
************** section editor picks *******************
we add new feild in news section editor_choice as boolean feild 

now in editor choice get all the editor_choice news and passed the data in index page


we have section as editor picks in home page so for that we want 8 news that should be picked by editor 

here we add more than 8 but for that list of news should be even divisible of 2 

now we have the logic to display the slider for two imgage in slider of we click in silder it add new image 
logic is for loop for main section of news and before end of for loop add condition of if forloop counter is divisible by 2 add div tag for slider like div of above the main section

<div class="item"> // tag of slider 
            <!-- for loop start -->
            {%for item in editor_choice_news %}
            <!-- main section -->
            <div class="post-block-wrapper clearfix mb-5">
                <div class="post-thumbnail">
                    <a href="{% url 'single-post' item.id %}">
                        <img class="img-fluid" src="{{item.img.url}}" alt="post-image"/>
                    </a>
                </div>
                <div class="post-content">
                    <h2 class="post-title mt-3">
                        <a href="{% url 'single-post' item.id %}">{{item.headline}} {{item.id}}</a>
                    </h2>
                    <div class="post-meta mb-2">
                        <span class="posted-time"><i class="fa fa-clock-o mr-2"></i>{{item.get_time}}</span>
                        <span class="post-author">
                            by
                            <a href="author.html">{{item.author_name}}</a>
                        </span>
                    </div>
                     <p>{{item.short_description}}</p>
                </div>
            </div>
            {% if forloop.counter|divisibleby:2 %}
                <div class="item">
           
            {%else%}
                </div>
        {%endif%}
    {%endfor%}
</div>

displays images like 12 23 34 45 56 67 78 89

but we want in 
1 3 5 7  
2 4 6 8
heee we successfully decode the logic for above pattern just some correction in code and we are able to solve it 
first our section  
        <div class="news-style-one-slide"> provide silde options
        <div class="item"> decide the rows 

after item section loop starts it prints first item then seconde item then applying the condition if forloop.counter|divisible by 2 if yes 
then end the iten section and again item section then loop starts again at counter 3 print item 3 at positon of 1 then print item 4 below item3 checks condition if counter 4 is divisible by 4 if yes end item new item continues till end 
and last but import outside the for loop the should be the end tag for item 

<div class="news-style-one-slide">
        <div class="item">
            <!-- for loop start -->
            {%for item in editor_choice_news %}
            <!-- main section -->
            <div class="post-block-wrapper clearfix mb-5">
                <div class="post-thumbnail">
                    <a href="{% url 'single-post' item.id %}">
                        <img class="img-fluid" src="{{item.img.url}}" alt="post-image"/>
                    </a>
                </div>
                <div class="post-content">
                    <h2 class="post-title mt-3">
                        <a href="{% url 'single-post' item.id %}">{{item.headline}} {{item.id}}</a>
                    </h2>
                    <div class="post-meta mb-2">
                        <span class="posted-time"><i class="fa fa-clock-o mr-2"></i>{{item.get_time}}</span>
                        <span class="post-author">
                            by
                            <a href="author.html">{{item.author_name}}</a>
                        </span>
                    </div>
                     <p>{{item.short_description}}</p>
                </div>
            </div>
            {% if forloop.counter|divisibleby:2 %}
            </div>
             <div class="item">
                
                {%endif%}
        {%endfor%}
    </div>

</div>

done with the slider logic for editor picks and new slider logic got 




*************************** taggit library ***********************
we are using the django-taggit library for tags defining by the user 
 it has tag model in built
 commnad ::: pip install django-taggit

 in setting.py include taggit in install apps
 INSTALLED_APPS = [
    ...
    'taggit'
]

create model category
import : from taggit.managers import TaggableManager
tags = TaggableManager()

The TaggableManager will show up automatically as a field in a ModelForm or in the admin. 
end taggit library not using anymore




**************** Profile management ********************
Creating the profile in navbar with the help of dropdown of bootstrap
added icon in it with the help of  font awesome
added user name and added padding and border radius for the div of dropdown

changing the search feild and searching the best serch tab in bootstrap
we found this 
<form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>

we assign padding and border-radius for profile in inline css
now i want to style all navbar elements which have dropdown so we inspect on dropdown and open the style tab which show css applied on that dropdown so tried all elements with padding and border radius and found the 
.main-navbar .dropdown:hover .dropdown-menu this tag

.main-navbar .dropdown:hover .dropdown-menu {
  transform: scaleY(1);
  opacity: 1;
  display: block;
  visibility: visible;
  padding: 10px; 
  border-radius :10px;
}

changing the content of profile like i want to add logout ,

Extendng user model as custom user with auth.user properties
import abstract user
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phoneNo = models.IntegerField(null=True)
    phoneNo2 = models.IntegerField(null=True)
    subscriberOfNewsletter = models.BooleanField(null=True)
    birth_date=models.DateField(null=True)
1.Create Create a Custom User Model 
import and  extend abstract user : from django.contrib.auth.models import AbstractUser

2.Update settings.py : AUTH_USER_MODEL = 'NewsBitApp.CustomUser'
import
from django.conf import settings

3.Create and Apply Migrations:
python manage.py makemigrations
python manage.py migrate

4.Update Forms and Admin:
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1) 

admin 

error : we not able to create customuser 
sol : 
delete database and get the database backup using the export import techinque of mysql database
delete the migration   and created again now it worked

now in views we have used user so switched to Customuser


****************** Tech Section ***********************
making dyamic tech dection in index.html 
fetched the data of tech category by passing the tech id as 4
passed the data to index.html page 
lets write the logic for displaying the news posts
we have main section row it contain all the news so in row section we haved to call the for loop

check loop work for single post so run successfully
<!-- loop starts  -->
        {%for item in tech_cat%}
        <div class="col-md-6 col-sm-6">
            <div class="post-block-wrapper clearfix">
                <div class="post-thumbnail">
                    <a href="{% url 'single-post' item.id %}">
                        <img class="img-fluid" src="{{item.img.url}}" alt="post-thumbnail"/>
                    </a>
                </div>
                <a class="post-category" href="{% url 'post-category' item.category_id %}">{{item.category_name}}</a>
                <div class="post-content">
                    <h2 class="post-title mt-3">
                        <a href="{% url 'single-post' item.id %}">{{item.headline}}</a>
                    </h2>
                    
                    
                    <div class="post-meta mb-2">
                        <span class="posted-time"><i class="fa fa-clock-o mr-2"></i>{{item.get_time}}</span>
                        <span class="post-author">
                            by
                            <a href="{% url 'author' 1 %}">{{item.author_name}}</a>
                        </span>
                    </div>
                    <p>{{item.short_description}}</p>
                        
                    </div>
                </div>
        </div>
        {%endfor%}

now add new div like we have in website 
so next div start <div class="col-md-6 col-sm-6"> </div>
in this div all the remaining items will display using loop 
for that inn if condition we have start this div and have to end div outside the loop such as :
 {%for item in tech_cat%}
            {% if forloop.counter == 1 %}
            <div class="col-md-6 col-sm-6">
                <div class="post-block-wrapper clearfix">
                    <div class="post-thumbnail">
                        <a href="{% url 'single-post' item.id %}">
                            <img class="img-fluid" src="{{item.img.url}}" alt="post-thumbnail"/>
                        </a>
                    </div>
                    <a class="post-category" href="{% url 'post-category' item.category_id %}">{{item.category_name}}</a>
                    <div class="post-content">
                        <h2 class="post-title mt-3">
                            <a href="{% url 'single-post' item.id %}">{{item.headline}}</a>
                        </h2>
                        
                        
                        <div class="post-meta mb-2">
                            <span class="posted-time"><i class="fa fa-clock-o mr-2"></i>{{item.get_time}}</span>
                            <span class="post-author">
                                by
                                <a href="{% url 'author' 1 %}">{{item.author_name}}</a>
                            </span>
                        </div>
                        <p>{{item.short_description}}</div>
                    </div>
                </div>

                <div class="col-md-6 col-sm-6">
            {%endif%}

        <!-- new section starts -->
                    <div class="post-list-block m-top-0">
                        <div class="post-block-wrapper post-float clearfix">
                            <div class="post-thumbnail">
                                <a href="{% url 'single-post' 1 %}">
                                    <img class="img-fluid" src="{% static 'images/news/news-04.jpg'%}" alt="post-thumbnail"/>
                                </a>
                            </div>
                            <div class="post-content">
                                <h2 class="post-title title-sm">
                                    <a href="{% url 'single-post' 1 %}">Intel’s new smart glasses actually look good</a>
                                </h2>
                                <div class="post-meta">
                                    <span class="posted-time"><i class="fa fa-clock-o mr-2"></i>7 hours ago</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    {%endfor%}
                </div>
            
tech section done
we have one problem as it display the first element again 

***************** Beauty Blog ************************

here we have to fetch the data for multiple ids or caategories so in filter add ids like 
    beauty_cat = news.objects.all().filter(Q(category_id =7 ) | Q(category_id=8 ) | Q(category_id=12 ) | Q(category_id=13))
Q()

Django Q objects:

Q object encapsulates a SQL expression in a Python object that can be used in database-related operations. Using Q objects we can make complex queries with less and simple code.

logic for slidder is slider class and item class are outside the for loop 
In for loop add if condition as if loop counter is divisibleby 2 => end item div and start new item div 
<!-- for loop start -->
        <div class="item">
            {%for item in beauty_cat%}

                    <div class="post-overlay-wrapper clearfix">
                        <div class="post-thumbnail">
                            <a href="{% url 'single-post' item.id %}">
                                <img class="img-fluid" src="{{item.img.url}}" alt="post-thumbnail"/>
                            </a>
                        </div>
                        <div class="post-content">
                            <a class="post-category white" href="{% url 'post-category' item.category_id %}">{{item.category_name}}</a>
                            <h2 class="post-title">
                                <a href="{% url 'single-post' item.id %}">On Beauty: Style and Fashion Blogger...</a>
                            </h2>
                            <div class="post-meta white">
                                <span class="posted-time">4 hours ago</span>
                                <span> by </span>
                                <span class="post-author">
                                    <a href="author.html">Jammy Anderson</a>
                                </span>
                            </div>
                        </div>
                    </div>

                {% if forloop.counter|divisibleby:2%}
                <!-- ending the item div -->
                    </div>
                    <div class="item">

                {%endif%}


            {%endfor%}
            <!-- item div -->
        </div>


**************** latest articles ***************
fetching the based on timeline 
it required the pagination logic 
so for right adding the slidebar


******************* Top authors *********************
for top authors we will required all authors nams ,images and news as posts 
so for that i have created a def funtion post count in auhtors model 
        def post_count(self):
                count = news.author_post_count(self)  
                return count
 and passed the all the info about author as self 
 and then call the news method which we have created as auhtor_post_count and passed parameter of authors info
        def author_post_count(self):
                count = news.objects.all().filter(author_id = self.id)
                return len(count)
    
in this function using orm retrive all the data as per auhtor and apply len funtion to return posts count
 display logic was simple just use for loop in widget-review.htm

we are going to change thr logic where i want post feild in author table which will store the count of posts
for that we want to assign count of posts in news model by 

above logic is also not suitable so back to original logic of fetching post count using function 
so we have initialize a list as posts and creted for loop to insert auhtors info to list thrn sort the list by postcount()
here we learn about sort() parameters sort () takes two parameter such as reverse true /false and second is key function 
so while sorting reverse true for sort according to descending order of postcount() 
key function where we have creaded a lambda funtion for postcount to order by postcount()
key used to do Comparion is based on this function.  

 lambda function is a small anonymous function


********************* Tour Game Health Hot News ***************

done 

********************* Logic for previous and next post in single-post page *********************************
9.single post next previous news  section and related posts section : these are news according to news sr of entered in news table we can pass the news id of previous news and next id of next news : done 
 done by creating a logic first of all take the news_id check if previous news ie news_id-1 and next news news_id+1 exists if exists the get the data and store it in the context which we will pass while rendering 

 we are using if exists because it prevent error if news not exists at id 

 then we encounters new error what id id is not in order like ids 1,2,3,5,8 like ids missing the we are not able to check previous or next headline to overcome this we can used loop i am using while loop because we have to run loop till the next id which has news or till end 

 then in the post-nav we encounter displaying error or unattractive nature so for that first of all check if previous posts exist if yes then start with  executing div statement of next post then check if next post exists 
  else part of previous if previous posts not exist then start with previous div and mention the content of next posts  which sees better than previous logic of frontend
    and we have comment the css property of display content for class post-navigation because if any post not it not well to see the 


done

issue:
 we have encounter the new worst case for the above logic where i have used the loop to find the next or previous post which may cause when post id is high or like 10 digits or unique characters id 
 sol:
 to resolve above issue we can first of all get all the ids from the table and store it list 

    all_news_id = news.objects.all().values_list('id',flat=True).order_by('id') 

 where values_list help to skip keys and flat true help retrieve a single value from each row of the queryset instead of a tuple.( to remove the ,)  

 but stil cause error to find index based on all_news_id because its type is queryset so convert it to list
    ids = list(all_news_id)
get the index by pasing the requested newsid 
    ind = ids.index(newsId)

now get the previous and next news details 
 if (news.objects.filter(id = listNewsId[indexFromList-1]).exists()):
            previous_news = news.objects.get(id = listNewsId[indexFromList-1])
            context["previous_news"]= previous_news
if (news.objects.filter(id = listNewsId[indexFromList+1]).exists()): 
                next_news = news.objects.get(id = listNewsId[indexFromList+1])
                context["next_news"]=next_news

but here we encounter an error when we reach to the end of list program search for next posts by len(list)+1 which cause error as list range out of range to handled this we have used the try except concept 
when this error cause we passed the index 0 manually in except block
if (news.objects.filter(id = listNewsId[indexFromList-1]).exists()):
            previous_news = news.objects.get(id = listNewsId[indexFromList-1])
            context["previous_news"]= previous_news
    try :
        if (news.objects.filter(id = listNewsId[indexFromList+1]).exists()): 
                next_news = news.objects.get(id = listNewsId[indexFromList+1])
                context["next_news"]=next_news
    except IndexError:
         if (news.objects.filter(id = listNewsId[0]).exists()): 
                next_news = news.objects.get(id = listNewsId[0])
                context["next_news"]=next_news

by using this logic we can create loop which will never ending for post for previous and next

************** Related Posts *******************
for related posts section can we the tag to display the posts whic means we will fetch the data for related tags
fetch the all mention tag for the posts :
     tag_list = new.tags.all()

created new object that will store the all the objects which above tag list
    related_posts = news.objects.all().filter(category_id__in = tag_list)

while creating above logic we failed to fetch data with multiple id to tags so from chatgpt we found id__in id__in is a type of lookup that allows you to filter querysets based on whether a model’s field matches any value in a provided list. The __in lookup is used to specify that the field value should be within a list of values.
When you use __in, you're asking Django's ORM (Object-Relational Mapping) to generate an SQL IN clause. This allows you to filter records where a field’s value matches any value in a given list or iterable.

done



************





************************Tasks ***********************
1.i want the slider for tags with multiple tags selection : done 
2.assign color to the tags like danger, info for background color : done 
4 new model for category : done
5 create model for editor picks where pass the news and editor can select 6-8 post from all posted news :done
sections required : done by adding an boolean field in news
6. slidebar logic for post by category : done
8.hot news ,tour ,game health : done
9.single post next previous news  section and related posts section : these are news according to news sr of entered in news table we can pass the news id of previous news and next id of next news : done 
11 most recent ,hot news, beauty blog,tech, latest artcile ,top authors : done
12we have one problem as it display the first element again : tech section : solve we just have to apply  else condition paste the remaining div for small dic which dont have headlines etc :done
13.categories page and navbar :done


user profile management: done half 
3 above error in comment like parents reply done but anyone reply to child does not shows on page
i have idea to display like instagram like if anyone reply to child then display it there only


7.pag logic for latest artcile in index.html

10. change the first static four news to multiple with slidder or changing according to the time


14 trending news in index.html navigation.htm based on the views 
15 search button use : done for news,categories,authors
16 navbar should be fixed 
17 use user info to all comment : done
18 user to author page or option
19 related news in single post should one for one tag :  done by distinct 
20 next previous according from whe re come like categories,author, or random : done
    https://www.w3schools.com/python/python_getstarted.asp
    https://www.w3schools.com/python/intro
    want to achieve this
21 tag models :done










NoReverseMatch at /post-category/2
Reverse for 'category_post' not found. 'category_post' is not a valid view function or pattern name. 