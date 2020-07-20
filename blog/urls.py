from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blogs_id>/', views.detail, name='detail'),
    path('<int:blogs_id>/author/', views.author_name, name='author'),
]