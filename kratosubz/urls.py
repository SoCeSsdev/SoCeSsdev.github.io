from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('home/', views.index, name='home'),  
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'), 
    path('blog/', views.blog, name='blog'),  
    path('about-us/', views.about_us, name='about_us'),  
    path('reseller/', views.reseller, name='reseller'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),  
    path('blog/post-1/', views.post_1, name='post_1'),  
    path('blog/post-2/', views.post_2, name='post_2'),  
    path('blog/post-3/', views.post_3, name='post_3'),  
    path('blog/post-4/', views.post_4, name='post_4'),  
    path('blog/post-5/', views.post_5, name='post_5'),  
    path('blog/post-6/', views.post_6, name='post_6'),  
    path('blog/post-7/', views.post_7, name='post_7'),  
    path('blog/post-8/', views.post_8, name='post_8'),  
    path('blog/post-9/', views.post_9, name='post_9'),  
    path('blog/post-10/', views.post_10, name='post_10'),  
  
]

