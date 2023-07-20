from django.urls import path

from . import views

urlpatterns = [
    path('post/examinations', views.handle_results, name='handle_results'),
]
