"""
URL configuration for NewsBit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="index"),
    path('index-2', views.index2,name="index-2"),
    path('about', views.about,name="about"),
    # path('account', views.account,name="account"),
    path('contact', views.contact,name="contact"),
    path('job-info', views.job_info,name="job-info"),
    path('job', views.job,name="job"),
    path('privacy', views.privacy,name="privacy"),
    path('search', views.search,name="search"),
    path('post-author/<str:authors_name>', views.post_author,name="post-author"),
    path('post-news/<str:news_details>', views.post_news,name="post-news"),
    path('post-full-width', views.post_full_width,name="post-full-width"),
    path('post-left-sidebar', views.post_left_sidebar,name="post-left-sidebar"),
    path('signup', views.signup,name="signup"),
    path('single-post/<int:newsId>/', views.single_post,name="single-post"),
    path('account', views.login,name="account"),
    path('terms', views.term,name="terms"),
    path('logout', views.logout,name="logout"),
    path('404', views.m404,name="404"),
    # path('single-post/<int:news_id>/postComment', views.postComment,name="postComment"),
    path('postComment', views.postComment,name="postComment"),
    path('search', views.search,name="search"),

    path('author/<int:author_id>/', views.author,name="author"),
    path('author/<int:author_id>/<int:newsId>/', views.author_posts,name="author_posts"),

    path('post-category/<int:category_id>', views.post_category,name="post-category"),
    path('post-category-1/<str:category_name>', views.post_category_1,name="post-category-1"),
    path('post-category/<int:category_id>/<int:newsId>/', views.category_posts,name="category_posts"),

]
