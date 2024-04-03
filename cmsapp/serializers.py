from rest_framework import serializers
from .models import ContentItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ContentItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = ContentItem
        fields = ['id', 'title', 'body', 'summary', 'document', 'categories']
