from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('config/', views.config, name='config'),
    path('new_person/', views.new_person, name='new_person'),
    path('remove/<int:pk>/', views.remove, name='remove'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]
