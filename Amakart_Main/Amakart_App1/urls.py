from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexClass.as_view(), name='index')
]