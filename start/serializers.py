from django.contrib.auth.models import Group, User
from rest_framework import serializers

# * This class creates "tables" with SQLite 
# ! I don´t know how they work
# ? But I learnig
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['urls', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']