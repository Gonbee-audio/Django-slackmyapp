from rest_framework import serializers
from slack.models import UserCreate

class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCreate
        fields = '__all__'