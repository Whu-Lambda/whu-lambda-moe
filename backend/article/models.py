from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField()
    author = models.CharField(max_length=64)
    cover = models.CharField(max_length=255)
    tags = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'
