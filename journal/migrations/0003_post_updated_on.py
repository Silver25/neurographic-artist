# Generated by Django 5.1.4 on 2025-01-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_post_excerpt_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
