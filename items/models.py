from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from django.utils import timezone
from .utils import item_image_path

class StatusChoices(Enum):
    LOST = 'LOST'
    FOUND = 'FOUND'

    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls]

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    contact_telegram = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=item_image_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="items", null=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices(), default=StatusChoices.LOST.value)

    @property
    def days_since_created(self):
        return (timezone.now() - self.created_at).days if self.created_at else None

    @property
    def comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments", null=True)

    @property
    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None