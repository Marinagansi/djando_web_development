from django.contrib import admin
from django.urls import path
from cloths import views

urlpatterns = [
    
    path('',views.firstpage),
    path('nav',views.nav),
    path('home',views.home),
    path('login',views.loginn),
    path('registration',views.registration),
      path('logout',views.logout_page),
        path('user_pannel',views.user_pannel),
        path('user_edit/<int:p_id>',views.edit),
        path('user_update/<int:p_id>',views.update),
     
   
]