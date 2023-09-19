# Generated by Django 4.2.3 on 2023-07-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'گروه', 'verbose_name_plural': 'گروه ها'},
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='blog.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='Article', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(verbose_name='وضعیت'),
        ),
    ]