# trips/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('trips/', views.TripList.as_view(), name='trip_list'),

    path('trips/<int:pk>',
        views.TripDetail.as_view(), name='trip_detail'),

    path('todos/', views.TodoList.as_view(), name='todo_list'),

    path('todos/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),


]