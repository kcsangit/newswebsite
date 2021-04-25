from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import *

page_path = 'frontend/pages/'

def index(request):
    data = {
        'title': "Home",
        'sliderData': Slider.objects.all(),
        'serviceData':Service.objects.all()

    }
    return render(request, page_path + 'home/home.html', data)


def about(request):
    data = {
        'title': "about",
        'numofclients':235,
        'numofprojects':525,
        'hourssupport':'1,223',
        'hardworkers':18,

        'testimoniallist':Testimonials.objects.all(),
        'clientlist':Clients.objects.all()
        

    }
    return render(request, page_path + 'about/about.html', data)

def services(request):
    data = {
        'title': "services",
        'servicelist':Service.objects.all()

    }
    return render(request, page_path + 'services/services.html', data)

def portfolio(request):
    data = {
        'title': "portfolio",
        'clientlist':Clients.objects.all()
        

    }
    return render(request, page_path + 'portfolio/portfolio.html', data)


def team(request):
    data = {
        'title': "team",
        'teamlist':Teams.objects.all()

    }
    return render(request, page_path + 'about/team/team.html', data)


def blog(request):
    news_list = News.objects.order_by('-id')
    paginator = Paginator(news_list,2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    data = {
        'page_obj':page_obj,
        'recentNews':News.objects.order_by('-id')[:3],
        'categoryData':Category.objects.prefetch_related('news_set')
    }
    return render(request,page_path+'blog/blog.html',data)
    


def blog_details(request,slug):

    get_news = News.objects.get(slug=slug)

    # return HttpResponse(get_news)
    data={
        'blogDetails':get_news
    }

    return render(request,page_path+'blog/blog-details.html',data)

    











def page_not_found(request,exception):
    return render(request, 'frontend/errors/404.html')


def slider_details(request, slug):
    data = {
        'sliderData': Slider.objects.get(slug=slug)
    }
    return render(request, page_path + 'slider/slider-details.html', data)
