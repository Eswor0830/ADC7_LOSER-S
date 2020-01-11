from django.urls import path
from .views import *
from .import views


urlpatterns = [
    path('hello/',view_hello_world),
    path('', views.freelancer_form,name='freelancer_insert'), # get and post req. for insert operation
    path('<int:id>/', views.freelancer_form,name='freelancer_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.freelancer_delete,name='freelancer_delete'),
    path('list/',views.freelancer_list,name='freelancer_list') # get req. to retrieve and display all records

]
