from rest_framework import viewsets
from rest_framework import routers
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'avatar', 'bio',
                  'reputation', 'created_at', 'updated_at']


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urls = router.urls
