from django.urls import path

from . import views

urlpatterns = [
    path('',views.Movie2_view, name = 'index')
]