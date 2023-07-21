from django.urls import path

from . import views

urlpatterns = [
    path('examinations', views.handle_results, name='handle_results'),
]
