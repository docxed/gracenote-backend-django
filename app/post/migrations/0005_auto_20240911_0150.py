# Generated by Django 5.1.1 on 2024-09-10 18:50

from django.db import migrations
from django.db import migrations, models
from django.conf import settings


def set_default_user(apps, schema_editor):
    Post = apps.get_model("post", "Post")
    User = apps.get_model(settings.AUTH_USER_MODEL)
    default_user = User.objects.get(pk=1)  # Replace with a valid user ID
    Post.objects.filter(created_by__isnull=True).update(created_by=default_user)


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_alter_post_created_by_alter_post_updated_by"),
    ]

    operations = [
        migrations.RunPython(set_default_user),
    ]