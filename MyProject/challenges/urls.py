from django.urls import path

from . import views

urlpatterns = [
    path('edit-profile', views.edit_profile),
    path('user-settings', views.index)
]