# Generated by Django 3.1.4 on 2021-01-15 13:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GK', '0002_auto_20201225_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
