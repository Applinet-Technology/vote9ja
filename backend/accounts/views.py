
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer


from django.shortcuts import render 

from django.contrib.auth import login

from django.contrib.auth import authenticate

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from knox.views import LoginView as KnoxLoginView

from .models import User


# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)
        
        
class LoginAPI(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user:
            return Response({
                "name": user.username,
                "token": user.auth_token.key
                
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=400)
            #status.HTTP_400_BAD_REQUEST)

class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class Person(object):
#     """docstring for Person"""
#     def __init__(self, arg):
#         super(Person, self).__init__()
#         self.arg = arg
        
class UserViewsetAPIView(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class BlogAPI(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class=BlogSerializer

#@csrf_exempt

# def user_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = User.objects.all()
#         serializer = UserSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)