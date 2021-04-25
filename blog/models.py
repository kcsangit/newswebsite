from django.db import models

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.

class ProjectConfig(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_fax = models.IntegerField(default=0)
    company_logo = models.ImageField(upload_to='logo')



class Slider(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='slider')
    is_first = models.BooleanField(default=0)
    description = RichTextField()

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    logo = models.CharField(max_length=200)

class Testimonials(models.Model):
    tname = models.CharField(max_length=100)
    tposition = models.CharField(max_length=100)
    tdescription  = RichTextField()
    timage = models.ImageField(upload_to='testimonials')

class Clients(models.Model):
    cimage = models.ImageField(upload_to = 'clients')


class Teams(models.Model):
    tname = models.CharField(max_length=100)
    tposition = models.CharField(max_length=100)
    tdescription  = RichTextField()
    timage = models.ImageField(upload_to='teams')
    twlink = models.CharField(max_length=255)
    fblink = models.CharField(max_length=255)
    instalink = models.CharField(max_length=255)
    linkedlink = models.CharField(max_length=255)




class Category(models.Model):
    created_at = models.DateTimeField(timezone.now())
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category')
    description = RichTextField()

    def __str__(self):
        return self.title


class News(models.Model):
    created_at = models.DateTimeField(timezone.now())
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='news', null=False)
    description = RichTextField()
    page_visit = models.IntegerField(default=0)
    