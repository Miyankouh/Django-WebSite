from django.urls import path 
from admin_panel import views

urlpatterns = [
    path('dashboard/', views.ArticlesListView.as_view(), name="admin_articles")
]
