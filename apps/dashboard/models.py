from __future__ import unicode_literals
from ..userdashboard.models import User
from django.db import models

# Create your models here.
class Posts(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name="created_post")


class Messages(models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="messages")
    post = models.ForeignKey(Posts, related_name="post",null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name="created_user")
