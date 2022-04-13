from rest_framework import generics, permissions  
from .models import Trip, Todo
from .serializers import TripSerializer, TodoSerializer
from .permissions import IsOwnerOrReadOnly
from pprint import pprint


class TripList(generics.ListCreateAPIView):
    # queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        print("REQ: " + str(self.request))
        pprint(vars(self.request))
        user = self.request.user
        print("REQ USER: " + str(self.request.user))
        print("REQ USER ID: " + str(self.request.user.id))
        return Trip.objects.filter(owner=self.request.user.id)


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