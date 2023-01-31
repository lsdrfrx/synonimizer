from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import serializers

from synonymizer_app.models import Profile


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        # возможна валидация формата данных
        user = authenticate(
            request=self.context["request"],
            username=attrs.get("username", ""),
            password=attrs.get("password", ""))

        if user:
            login(self.context["request"], user)
        else:
            raise serializers.ValidationError("401 Unauthorized", code=401)

        attrs["user"] = user

        return attrs


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    nickname = serializers.CharField()

    def validate(self, attrs):
        try:
            username = attrs["username"]
            password = attrs["password"]
            email = attrs["email"]
            nickname = attrs["nickname"]
        except KeyError:
            raise serializers.ValidationError("400 Bad request", code=400)

        if User.objects.filter(username=attrs["username"]):
            raise serializers.ValidationError("400 Bad request (username is already used)", code=400)

        if User.objects.filter(email=attrs["email"]):
            raise serializers.ValidationError("400 Bad request (email is already used)", code=400)

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"])

        return Profile.objects.create(nickname=validated_data["nickname"], user=user)
