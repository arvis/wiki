from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_entries, name='index'),
    path('<str:entry_title>/', views.view_entry, name='view_entry'),
    path('create/', views.create_entry, name='create_entry'),
    path('<str:entry_title>/create', views.create_entry_with_title, name='create_entry_with_title'),
    path('<str:entry_title>/edit/', views.view_entry, name='view_entry'),

]