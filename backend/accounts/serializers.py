
'''
from .models import User, Blog
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','get_full_name', 'birthdate', 'gender', 'email', 'phone_number', 'state', 'lga', 'ward', 'password']
        
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            state=validated_data['state'],
            lga=validated_data['lga'],
            ward=validated_data['ward'],
            
            
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        

        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['category', 'title', 'body', 'date', 'blogger', 'username']
        order_by = ['date',]'''