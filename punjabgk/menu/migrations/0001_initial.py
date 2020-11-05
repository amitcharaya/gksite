# Generated by Django 3.1.2 on 2020-10-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=70, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.TextField(max_length=100, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
            ],
        ),
    ]
