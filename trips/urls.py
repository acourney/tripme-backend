# trips/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # GET localhost:8000/trips
    # POST localhost:8000/trips
    path('trips/', views.TripList.as_view(), name='trip_list'),
    # PUT localhost:8000/trips/:id
    # DELETE localhost:8000/trips/:id
    path('trips/<int:pk>',
        views.TripDetail.as_view(), name='trip_detail'),
    # GET localhost:8000/todos
    # POST localhost:8000/todos
    path('todos/', views.TodoList.as_view(), name='todo_list'),
    # PUT localhost:8000/todos/:id
    # DELETE localhost:8000/todos/:id
    path('todos/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),

    # path('members/', views.TripMemberList.as_view(), name='member_list'),
    # path('members/<int:pk>', views.TripMemberDetail.as_view(), name='member_detail'),

]