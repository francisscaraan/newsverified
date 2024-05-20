from django.urls import path
from . import views

urlpatterns = [
    path('newsverified/', views.newsverified, name='newsverified'),
]