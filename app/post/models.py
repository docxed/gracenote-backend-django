from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    imageUrl = models.ImageField(upload_to="post/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "authen.User",
        on_delete=models.CASCADE,
        related_name="created_by",
    )
    updated_by = models.ForeignKey(
        "authen.User",
        on_delete=models.CASCADE,
        related_name="updated_by",
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title
