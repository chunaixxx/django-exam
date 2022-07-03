from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from django.db.models import Q
from .serializers import TodoSerializer, CategorySerializer
from .models import Todo, Category
from rest_framework import filters

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['deadline']


class NotDoneTodoViewSet(ModelViewSet):
    queryset = Todo.objects.filter(Q(status='PLANNED') | Q(status='PROCESS'))
    serializer_class = TodoSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
