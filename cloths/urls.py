from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
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
        path('password_reset/',

         auth_views.PasswordResetView.as_view(

             template_name='password/password_reset_form.html'),

         name='password_reset'),



    path('password_reset/done/',

         auth_views.PasswordResetDoneView.as_view(

             template_name='password/password_reset_done.html'),

         name='password_reset_done'),



    path('reset/<uidb64>/<token>/',

         auth_views.PasswordResetConfirmView.as_view(

             template_name='password/password_reset_confirm.html'),

         name='password_reset_confirm'),



    path('reset/done/',

         auth_views.PasswordResetCompleteView.as_view(

             template_name='password/password_reset_complete.html'),

         name='password_reset_complete'),
     
]