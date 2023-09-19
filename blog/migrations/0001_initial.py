# Generated by Django 4.2.3 on 2023-07-26 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='موضوع')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='هدف')),
                ('decription', models.TextField(verbose_name='متن')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('publsihDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('updateDate', models.DateField(auto_now=True)),
                ('picture', models.ImageField(upload_to='images', verbose_name='تصویر')),
                ('status', models.CharField(choices=[('I', 'پیش نویس'), ('W', 'نوشته شده')], max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='نام')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='هدف')),
                ('status', models.CharField(choices=[('S', 'نمایش'), ('N', 'عدم نمایش')], max_length=1, verbose_name='وضعیت')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
