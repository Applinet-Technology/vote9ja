

'''
from django.shortcuts import render 

from django.contrib.auth import authenticate

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, BlogSerializer

from .models import User, Blog

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)
        
        
class LoginAPI(APIView):
    #permission_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                "name": user.get_full_name,
                "token": user.auth_token.key
                
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=400)
            #status.HTTP_400_BAD_REQUEST)



class UserViewset(viewsets.ModelViewSet):
    #permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BlogAPI(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer'''