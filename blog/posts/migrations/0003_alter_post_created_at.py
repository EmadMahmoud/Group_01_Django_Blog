# Generated by Django 4.1 on 2022-08-28 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_publishing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
