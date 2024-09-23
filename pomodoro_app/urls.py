from django.urls import path
from . import views

urlpatterns = [
    path('', views.pomodoro_view, name='pomodoro'),
    path('save_session/', views.save_session, name='save_session'),
    path('get_sessions/', views.get_sessions, name='get_sessions'),
]