# Generated by Django 5.1.7 on 2025-03-16 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='create_ed',
            new_name='created_ed',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='update_ed',
            new_name='updated_ed',
        ),
    ]
