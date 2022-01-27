from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    
    path('customerform',views.customerform),
    path('signin',views.signin),
    path("c_pannel",views.customer_pannel),
    path("c_edit/<int:p_id>",views.edit),
    path('customer_update/<int:p_id>',views.update),
    path("c_delete/<int:p_id>",views.delete),
    
      
]