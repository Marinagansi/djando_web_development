from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    
    path('storeform',views.storeform),
      path('shop',views.stores),
      path('cloth_pannel',views.cloths),
       path('cloth_edit/<int:p_id>',views.edit),
       path('cloth_update/<int:p_id>',views.update),
       path('cloth_delete/<int:p_id>',views.delete),
        path('adminnn',views.adminn),
          path('cloth_details/<int:p_id>',views.cloth_details),
    path('searched',views.search_cloth),
]