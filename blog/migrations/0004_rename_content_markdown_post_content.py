# Generated by Django 5.0.6 on 2024-06-25 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_content_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_markdown',
            new_name='content',
        ),
    ]