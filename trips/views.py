from rest_framework import generics, permissions  
from .models import Trip, Todo
from django.db.models import Q
from .serializers import TripSerializer, TodoSerializer
from .permissions import IsOwnerOrReadOnly
from pprint import pprint


class TripList(generics.ListCreateAPIView):

    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(Q(members__in=[self.request.user]) | Q(owner=self.request.user)).distinct()

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]



class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]