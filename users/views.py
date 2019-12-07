from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, TokenHasScope
)
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
