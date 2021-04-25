from django.urls import path
from . import views

from django.http import Http404


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('slider/<slug>', views.slider_details, name='slider-details'),
    path('team',views.team,name='team'),
    path('services',views.services,name='services'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('blog',views.blog,name='blog'),
    path('blog/details/<slug>',views.blog_details,name='blog_details'),
    
       
]