from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializer import UserSerializer
from users.rql_filter import RQLFilterBackend


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (RQLFilterBackend,)
