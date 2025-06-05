from rest_framework import viewsets
from .models import Article
from .serializers import ArticleListSerializer, ArticleViewSerializer
from django.http import HttpResponse

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ArticleViewSerializer
        return ArticleListSerializer

    def home_view(request):
    return HttpResponse("""
        <h1>Добро пожаловать в музыкальный сервис!</h1>
        <p><a href="/admin/">Админка</a></p>
        <p><a href="/api/articles/">API статей</a></p>
    """)