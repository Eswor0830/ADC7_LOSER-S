from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',view_hello_world),
]
