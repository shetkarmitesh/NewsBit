from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import news,Author,Comment,Category
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    new = news.objects.all()[:4] 
    editor_choice_news = news.objects.all().filter(editor_choice=True)
    # applying the length of 5 
    tech_cat = news.objects.all().filter(category_id =5)[:6]
    beauty_cat = news.objects.all().filter(Q(category_id =7 ) | Q(category_id=8 ) | Q(category_id=12 ) | Q(category_id=13))
    latest_article  = news.objects.all().order_by('-datetime')
    top_authors = Author.objects.all()
    # print(top_authors[0].post_count(0))
    # for i in top_authors:
    #     print(i.id,i.first_name,i.post_count())
    # print(len(latest_article),latest_article[0].headline,latest_article[17].get_time())
    return render(request,'index.html',{'news':new,'editor_choice_news':editor_choice_news,'tech_cat':tech_cat,'beauty_cat':beauty_cat,'latest_article':latest_article,'top_authors':top_authors})


def index2(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def account(request):
    return render(request,'index.html')

def author(request,author_id):
    author_details = Author.objects.get(id=author_id)
    # print(author_details.id,author_details.first_name,"asdaaaasdadadadsa")
    news_details = news.objects.all().filter(author_id = author_details.id)
    return render(request,'author.html',{'author_detail':author_details,"news":news_details})

def contact(request):
    return render(request,'index.html')
def job_info(request):
    return render(request,'index.html')
def job(request):
    return render(request,'index.html')
def privacy(request):
    return render(request,'index.html')
def search(request):
    return render(request,'index.html')

def term(request):
    return render(request,'index.html')

def search(request):
    return render(request,'index.html')

def post_category_1(request):
    return render(request,'index.html')
def post_full_width(request):
    return render(request,'index.html')

def post_left_sidebar(request):
    return render(request,'index.html')
def m404(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="POST":
        # fetching the data from form
        first_name = request.POST['f-name']
        last_name = request.POST['l-name']
        email = request.POST['email-address']
        password1 = request.POST['password-s']
        password2= request.POST['password-c']

        # adding the data to database
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "The user is alredy taken")
                return redirect('signup')
            user = User.objects.create_user(username=email,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            # messages.info(request, "user created successfully")
            return redirect('/')
        else: 
            messages.info(request, "password not matching")
            return redirect('signup')
         
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        # fetching the data from form
        username = request.POST['loginemail']
        password = request.POST['loginPassword']
        user = auth.authenticate(username=username ,password=password)
        if user is not None: 
            auth.login(request,user)
            # request.session["member_id"] = request.user.id
            return redirect('/')
        else: 
            messages.info(request,"invalid credentails")
            redirect('account')
    return render (request,'account.html')



def logout(request):
    auth.logout(request)
    return render(request,'index.html')


def single_post(request,newsId):
    new = news.objects.get(id=newsId)
    # print(new.headline,len(new.tags.all()))
    # for i in new.tags.all():
    #     print(i.id)
    parentComments = Comment.objects.all().filter(post_id = new.id,parent_comment_id=None)
    subComments = Comment.objects.all().filter(post_id = new.id).filter(~Q(parent_comment_id=None)).order_by('parent_comment_id')
    # print(len(subComments),"p0000000000000000000000000")
    # for i in subComments :
    #     print(i.author_id,i.author_name())
    return render(request,'single-post.html',{'news':new,'parentComments':parentComments,'subComments':subComments})

def postComment(request):
    if request.method =="POST":
        
        
        news_id = request.POST['news_id']
        author_id = request.POST['author_id']
        # author_name = request.POST['author_name']
        # email = request.POST['email']
        content = request.POST['content']
        parentComment_id = request.POST['parentComment_id']
        if parentComment_id is not None :

            comment = Comment.objects.create(post_id = news_id,author_id = author_id,content = content,user_id=request.user.id,parent_comment_id=parentComment_id )
        else:
            comment = Comment.objects.create(post_id = news_id,author_id = author_id,content = content,user_id=request.user.id )

        return redirect('single-post',news_id)

    return render(request,"single-post.html")

def post_category(request,category_id):
    news_details = news.objects.all().filter(tags = category_id)
    title = Category.objects.get(id =category_id)
    
    return render(request,'post-category-2.html',{'news':news_details,'title':title})