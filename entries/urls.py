from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_entries, name='index'),
    path('create/', views.create_entry, name='create_entry'),
    path('entry/<str:entry_title>/', views.view_entry, name='view_entry'),
    path('entry/<str:entry_title>/edit/', views.edit_entry, name='edit_entry'),
    # path('<str:entry_title>/create', views.create_entry_with_title, name='create_entry_with_title'),

]