# Generated by Django 3.1.2 on 2020-12-13 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20201213_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategories',
            old_name='subcat',
            new_name='subcatagory',
        ),
    ]
