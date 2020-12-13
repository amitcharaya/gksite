from django.urls import path,include


from . import views
app_name='menu'
urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('aboutus/',views.about,name="about"),
    path('courses/',views.courses,name="courses"),


    path('contact/',views.contact,name="contact"),
    path("message/", views.message,name="message"),
    path("GK/", include("GK.urls")),
    path("category/<int:id>/",views.category,name="category"),
    path("postdetail/<int:id>/",views.postdetail,name="postdetail"),
    path("subcategory/<int:id>/",views.subcategory,name="subcategory"),
]