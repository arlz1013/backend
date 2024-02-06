from rest_framework import serializers
from ..models.UsersModel import Users

# * This class make a Convertion about Datas
# todo Convierte la Informacion de Los Modelos
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
                    'name', 
                    'pasw', 
                    'status'
                ]
