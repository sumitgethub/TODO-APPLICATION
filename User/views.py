from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.serializers import UserLoginSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from User.utils import get_custom_jwt_token





#user register api
class UserRegistrationView(APIView):


    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            User = serializer.save()
            token = get_custom_jwt_token(User)
            return Response({'token': token, 'msg': 'Registration Success'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user login api
class UserLoginView(APIView):


    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_custom_jwt_token(user)
                return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
            return Response({'error': {'non_field_errors': ['username or password is not valid']}}, status=status.HTTP_400_BAD_REQUEST)






