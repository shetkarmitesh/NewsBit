from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import news,Author,Comment
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    new = news.objects.all()[:4] 
    
    return render(request,'index.html',{'news':new})


def index2(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def account(request):
    return render(request,'index.html')

def author(request,author_id):
    author_details = Author.objects.get(id=author_id)
    print(author_details.id,author_details.first_name,"asdaaaasdadadadsa")
    return render(request,'author.html',{'author_detail':author_details})

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
def post_category_2(request):
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
    parentComments = Comment.objects.all().filter(post_id = new.id,parent_comment_id=None)
    subComments = Comment.objects.all().filter(post_id = new.id).filter(~Q(parent_comment_id=None)).order_by('parent_comment_id')
    print(len(subComments),"p0000000000000000000000000")
    for i in subComments :
        print(i.author_id,i.author_name())
    return render(request,'single-post.html',{'news':new,'parentComments':parentComments,'subComments':subComments})

def postComment(request,news_id):
    if request.method =="POST":
        return redirect('/')

    return render(request,"single-post.html")