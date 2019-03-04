from rest_framework.serializers import ModelSerializer, CharField, ValidationError, Serializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('date_joined', 'last_login')