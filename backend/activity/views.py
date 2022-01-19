from rest_framework import viewsets
from rest_framework import routers
from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


router = routers.SimpleRouter()
router.register(r'activities', ActivityViewSet)

urls = router.urls
