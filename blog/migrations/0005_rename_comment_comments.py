# Generated by Django 4.2.7 on 2024-06-04 13:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
