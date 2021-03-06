# Generated by Django 3.1 on 2021-04-21 11:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
                ('tposition', models.CharField(max_length=100)),
                ('tdescription', ckeditor.fields.RichTextField()),
                ('timage', models.ImageField(upload_to='teams')),
                ('twitterlink', models.CharField(max_length=255)),
                ('facebooklink', models.CharField(max_length=255)),
                ('instalink', models.CharField(max_length=255)),
                ('linkedinlink', models.CharField(max_length=255)),
            ],
        ),
    ]
