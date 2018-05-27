from django.urls import path

from . import views

urlpatterns = [
    path('mine/', views.index, name='index')
]