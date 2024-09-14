from django.core.management.base import BaseCommand
from post.models import Post
from authen.models import User


class Command(BaseCommand):
    help = "Set default created_by user for all posts"

    def handle(self, *args, **kwargs):
        default_user = User.objects.get(pk=1)  # Replace with the actual default user ID
        Post.objects.filter(created_by__isnull=True).update(created_by=default_user)
