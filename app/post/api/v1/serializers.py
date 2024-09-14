from rest_framework import serializers
from post.models import Post
from django.core.validators import FileExtensionValidator


class PostSerializer(serializers.ModelSerializer):
    imageUrl = serializers.ImageField(
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"])
        ]
    )

    created_by_name = serializers.CharField(
        source="created_by.first_name", read_only=True
    )
    updated_by_name = serializers.CharField(
        source="updated_by.first_name", read_only=True
    )
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]

    def get_created_by(self, obj):
        return f"{obj.created_by.first_name} {obj.created_by.last_name}"

    def get_updated_by(self, obj):
        return f"{obj.updated_by.first_name} {obj.updated_by.last_name}"

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        validated_data["updated_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user
        return super().update(instance, validated_data)
