# Generated by Django 3.1.5 on 2021-01-21 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptiono',
            new_name='description',
        ),
    ]
