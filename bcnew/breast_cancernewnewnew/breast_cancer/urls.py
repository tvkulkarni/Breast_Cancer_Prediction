from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/about/',views.about),
    path('',views.homepage),  
    path('evaluser',views.evaluser) , 
]

