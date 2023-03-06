from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserDetail

class UserDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        fields = '__all__'


