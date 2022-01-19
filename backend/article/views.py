from rest_framework import viewsets
from rest_framework import routers
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)

urls = router.urls
