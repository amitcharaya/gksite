from django.db import models
class Question_Type(models.Model):
    question_type = models.CharField(max_length=50,default="none")
    def __str__(self):
        return self.question_type

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date_published')
    choice1_text=models.CharField(max_length=200)
    choice2_text = models.CharField(max_length=200)
    choice3_text = models.CharField(max_length=200)
    choice4_text = models.CharField(max_length=200)
    answer_text=models.CharField(max_length=200)
    notes = models.TextField(max_length=25500, blank=True, null=True)
    question_type_cat = models.ForeignKey(Question_Type,on_delete=models.CASCADE,default=1)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.question_text

