from django.utils.encoding import smart_str
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from .models import Message,Menus,Categories,Postdetail,SubCategories
import os
import requests

from punjabgk.settings import BASE_DIR, STATIC_ROOT

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        print(name)
        print(password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            return  redirect('/login/')
    else:
        return render(request,"menu/login.html")
def logout(request):
    auth.logout(request)
    return redirect("/login/")
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    menus=Menus.objects.all()
    context={"menus":menus}
    return render(request, "menu/index.html",context)

def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "menu/about-us.html")

def courses(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "menu/courses.html")

def category(request,id):
    menus=Menus.objects.all()
    category=Categories.objects.filter(menu_related=id)
    context={"categories":category,"menus":menus}
    return render(request, 'menu/category.html', context)

def subcategory(request,id):
    menus=Menus.objects.all()
    category=SubCategories.objects.filter(category=id)
    context={"subcategories":category,"menus":menus}
    return render(request, 'menu/category.html', context)


def postdetail(request,id):
    menus = Menus.objects.all()

    postdetail=Postdetail.objects.filter(subcategory=id)
    context={"postdetails":postdetail,"menus":menus}
    return render(request, 'menu/postdetail.html', context)


def contact(request):
    # return HttpResponse('Hello from Python!')
    menus = Menus.objects.all()
    context = {"menus": menus}
    return render(request, "menu/contact.html",context)

def message(request):
    try:
        msg=Message()
        msg.name=request.POST.get('name')
        msg.subject=request.POST.get('subject')
        msg.email=request.POST.get('email')
        msg.message=request.POST.get('message')
        msg.save()
        messages.info(request,"Thank You! Your Message sent")
        return redirect('contact')
    except:
        messages.info(request, "Sorry Something went wrong Try again")
        return redirect('contact')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        password1= request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email):
                messages.info(request,"Email alredy exist")
                return redirect('register')
            else:

                user=User.objects.create_user(username=email,email=email,password=password1,first_name=name)
                user.save()
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request, "Password do not match")
            return redirect('register')
    else:
        return render(request, "menu/register.html")


def download(request):

    # mimetype is replaced by content_type for django 1.7
    filename=os.path.join(os.path.abspath('staticfiles'),"PdfBulk.msi")
    serverfile=open(filename,"rb")
    response = HttpResponse(serverfile,content_type='application/force-download')
    print(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('Pdf Bulk.msi')
    response['Content-Length'] = os.stat(filename).st_size
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response







