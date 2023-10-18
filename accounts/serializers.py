from rest_framework import serializers
from .models import Passwords


class PasswordSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Passwords
        fields='__all__'