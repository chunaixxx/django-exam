from rest_framework.serializers import ModelSerializer
from .models import Todo, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(ModelSerializer):
    category_info = CategorySerializer(source='category', many=True)
    class Meta:
        model = Todo
        exclude = ['category']