# Generated by Django 4.1.8 on 2023-04-30 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='images',
            new_name='image',
        ),
    ]