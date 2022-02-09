from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    
    # path('booking/<int:p_id>',views.booking),
    path('booking_pannel',views.booking_pannel),
    path('booking_edit/<int:p_id>',views.edit),

    path('booking_update/<int:p_id>',views.book_update),
    path('booking_delete/<int:p_id>',views.delete),
    path('user_profile/<int:p_id>',views.Userprofile),
    
     
   
]