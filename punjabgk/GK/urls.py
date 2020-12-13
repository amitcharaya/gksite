from django.urls import path
from . import views

app_name='GK'
urlpatterns=[
    path('questions/<int:id>/',views.index,name='questions'),

    path('',views.home,name='home'),
    path('<int:pk>/',views.DetailView.as_view(),name='details'),
    path('next/<int:questionid>/',views.next,name='next'),
    path('pre/<int:questionid>/',views.pre,name='pre'),
]