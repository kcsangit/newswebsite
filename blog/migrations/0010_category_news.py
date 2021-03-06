# Generated by Django 3.1 on 2021-04-24 05:09

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20210421_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 24, 5, 9, 47, 784202, tzinfo=utc))),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='category')),
                ('is_first', models.BooleanField(default=0)),
                ('description', ckeditor.fields.RichTextField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 24, 5, 9, 47, 785167, tzinfo=utc))),
                ('status', models.BooleanField(default=0)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='news')),
                ('description', ckeditor.fields.RichTextField()),
                ('page_visit', models.IntegerField(default=0)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
