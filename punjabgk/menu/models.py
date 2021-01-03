from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Menus(models.Model):
    menuname=models.CharField(max_length=20)

    def __str__(self):
        return self.menuname

class Categories(models.Model):
    haeding=models.CharField(max_length=100)
    menu_related=models.ForeignKey(Menus,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.haeding

class SubCategories(models.Model):
    subcatagory=models.CharField(max_length=100)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.subcatagory

class Postdetail(models.Model):
    haeding = models.CharField(max_length=100)
    detail = RichTextField(null=True, blank=True)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.haeding


class Message(models.Model):
    name=models.TextField('name',max_length=70)
    email=models.EmailField('email')
    subject=models.TextField('subject',max_length=100)
    message=models.TextField('message')

    def __str__(self):
        return self.subject