from django.urls import path
from . import views

urlpatterns = [
    path('addTsk/', views.addTask, name='addTask'),
]