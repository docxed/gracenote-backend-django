from rest_framework import serializers
from authen.models import User
from django.db import models


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "sex",
            "phone",
            "imageUrl",
            "created_at",
            "updated_at",
            "password",
        ]
        indexes = [
            models.Index(fields=["email"]),
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            birth_date=validated_data["birth_date"],
            sex=validated_data["sex"],
            phone=validated_data["phone"],
            imageUrl=validated_data["imageUrl"],
        )
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]

    def save(self, **kwargs):
        user = self.context["request"].user
        if not user.check_password(self.validated_data["old_password"]):
            raise serializers.ValidationError("Old password is incorrect")
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user
