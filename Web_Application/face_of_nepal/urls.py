from django.contrib import admin
from django.urls import path, include
from face_of_nepal.views import *
from .views import Freelancer_list

urlpatterns =[   
    #path('hostel/',freelancer_list), 
    path('freelancerform/',freelancer_form),
    path('freelancerform/save',freelancer_save),
    path('freelancer/edit/<int:ID>',freelancer_edit),
    path('freelancer/edit/update/<int:ID>',freelancer_update_save),
    path('freelancer/delete/<int:ID>',freelancer_delete),
    path('search/',search),
    path('upload/',upload),
    path('download/',download)
    
]
