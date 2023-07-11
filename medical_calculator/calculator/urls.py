from django.urls import path

from . import views

urlpatterns = [
    path('', views.handle_results, name='handle_results'),
]
