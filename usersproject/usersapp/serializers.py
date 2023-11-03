from rest_framework import serializers
from .models import *

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id', 'username', 'email','password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ('id', 'username', 'email','password')
