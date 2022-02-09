from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
path('contact',views.contactpage),
path('message',views.message),
]