# Generated by Django 4.2.3 on 2023-07-28 13:17

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options_category_category_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('obejects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='blog.category', verbose_name='زیر مجموعه'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(verbose_name='نمایش'),
        ),
    ]
