from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('add/<int:a>/<int:b>',views.add),
    path('Employee_list/',views.Employee_list)

]
