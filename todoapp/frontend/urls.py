from django.urls import  path, include
from . import views


urlpattern = [
    path('',views.index)
]