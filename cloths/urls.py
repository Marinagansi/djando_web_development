from django.contrib import admin
from django.urls import path
from cloths import views

urlpatterns = [
    
    path('',views.firstpage,name='firstpage'),
    path('nav',views.nav),
    path('home',views.home,name='home'),
    path('login',views.loginn),
    path('registration',views.registration,name='create'),
      path('logout_admin',views.logout_page),
        path('user_pannel',views.user_pannel),
        path('user_edit/<int:p_id>',views.edit,name='edit'),
        path('user_update/<int:p_id>',views.update,name='update'),
        path('user_delete/<int:p_id>',views.delete,name='delete'),
        path('admin2',views.admin2,name='adminn'),
     
   
]