from rest_framework import serializers
from django.contrib.auth import get_user_model
import hashlib

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Manually hash the password using SHA-256
        password = validated_data['password']
        # hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            # password=hashed_password
        )
        print("saved Password in serializers create function: ", password)
        user.set_password_1(password)
        user.save_user()
        print("Came back from the save_user function ")
        return user
