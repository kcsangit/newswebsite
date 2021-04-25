from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(ProjectConfig)
class AdminProject(admin.ModelAdmin):
    list_display = ['company_name','company_email']

@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title','slug','is_first']
    prepopulated_fields  = {'slug':['title',]}

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['id','title']
    
@admin.register(Testimonials)
class AdminTestimonials(admin.ModelAdmin):
    list_display  = ['id','tname','tposition']

@admin.register(Clients)
class AdminClients(admin.ModelAdmin):
    pass

@admin.register(Teams)
class AdminTeams(admin.ModelAdmin):
    list_display  = ['id','tname','tposition']


@admin.register(Category)

class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'posted_by']
    prepopulated_fields  = {'slug':['title',]}


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'posted_by', 'category_id']
    prepopulated_fields = {'slug': ['title', ]}
