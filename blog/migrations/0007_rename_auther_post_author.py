# Generated by Django 4.2.7 on 2024-06-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comments_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
    ]
