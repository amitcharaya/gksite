from django.db import models
from ckeditor.fields import RichTextField
class Question_Type(models.Model):
    question_type = models.CharField(max_length=50,default="none")
    def __str__(self):
        return self.question_type

class Question(models.Model):
    question_text=RichTextField(null=True, blank=True)
    pub_date=models.DateTimeField('date_published')
    choice1_text=models.CharField(max_length=200)
    choice2_text = models.CharField(max_length=200)
    choice3_text = models.CharField(max_length=200)
    choice4_text = models.CharField(max_length=200)
    answer_text=models.CharField(max_length=200)
    notes = RichTextField(null=True, blank=True)
    question_type_cat = models.ForeignKey(Question_Type,on_delete=models.CASCADE,default=1)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.question_text


