from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from .models import Passwords
from .serializers import PasswordSerializers
# Create your views here.

class Generate(APIView):
    def post(self,request,format=None):
        
        length = request.data['passwordLength']
        uppercase = request.data['includeUppercase']
        numbers = request.data['includeNumbers']
        symbols = request.data['includeSymbols']

        chars = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers_values = '1234567890'
        symbol_values = '!@#$%&*()'
        try:
            if uppercase:
                chars+=uppercase_values
            if numbers:
                chars+=numbers_values
            if symbols:
                chars+=symbol_values
            password = ''
            for i in range(length):
                password+=random.choice(chars)
            return Response(password)
        except Exception as e:
            print(e)
            return Response(str(e))
class SavePasswords(APIView):
    def post(self,request,format=None):
        try:

            password = request.data['password']
            
            serializer = PasswordSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message':'Success'})
        except Exception as e:
            return Response(str(e))
class ShowPasswords(APIView):
    def get(self,request,format=None):
        try:
            saved_pass = Passwords.objects.all()
            serializer = PasswordSerializers(saved_pass,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(str(e))
