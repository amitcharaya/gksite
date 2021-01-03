import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question,Question_Type
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator

def index(request,id):
    qt = Question_Type.objects.all()

    question = Question.objects.filter(published=True, question_type_cat=id)
    paginator=Paginator(question,10)
    page=request.GET.get('page')
    questions=paginator.get_page(page)

    context = {'questions': questions,'qt':qt}
    return render(request, 'GK/Todays.html', context)




class DetailView(generic.DetailView):
    model = Question
    template_name = "GK/details.html"

def home(request):
    qt = Question_Type.objects.all()
    context = {'qt': qt}

    return render(request, 'GK/index.html',context)


def next(request,questionid):
    try:
        questionid=questionid+1
        question = Question.objects.get(pk=questionid)
        context = {'question': question}
        return render(request, 'GK/details.html', context)
    except:
        questionid = questionid 
        question = Question.objects.get(pk=questionid)
        context = {'question': question,"error_message":"You are done for the day!"}
        return render(request, 'GK/details.html', context)

def pre(request,questionid):
    try:
        questionid=questionid-1
        question = Question.objects.get(pk=questionid)
        context = {'question': question}
        return render(request, 'GK/details.html', context)
    except:
        questionid = questionid 
        question = Question.objects.get(pk=questionid)
        context = {'question': question,"error_message":"This is First Question"}
        return render(request, 'GK/details.html', context)

# Create your views here.
