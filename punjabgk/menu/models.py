from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)



class Message(models.Model):
    name=models.TextField('name',max_length=70)
    email=models.EmailField('email')
    subject=models.TextField('subject',max_length=100)
    message=models.TextField('message')

    def __str__(self):
        return self.subject