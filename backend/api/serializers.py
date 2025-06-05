from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'tags', 'created_at', 'author', 'image']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # Убедитесь, что модель Article импортирована
        fields = '__all__'  # Или укажите конкретные поля