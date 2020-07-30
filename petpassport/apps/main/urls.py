from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('create_record', views.create_record, name= 'create_record'),
    path('about', views.about, name= 'about')
    ]
