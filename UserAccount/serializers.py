from django.contrib.auth.models import User
from rest_framework import  serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs={
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'res': 'Password must match.'})

        user.set_password(self.validated_data['password'])
        user.save()

        return user


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs={
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        user = User.objects.get(username=self.validated_data['username'])

        if user is not None:
            print(instance)
            username = self.validated_data['username']
            email = self.validated_data['email']
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'res': 'Password must match.'})

        user.set_username(username)
        user.set_email(email)
        user.set_password(self.validated_data['password'])
        user.save()

        return user
