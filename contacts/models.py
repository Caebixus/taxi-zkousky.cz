from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    feedbackUser = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("User"), on_delete=models.CASCADE)
    message = models.TextField()
    message_published = models.DateTimeField(auto_now_add=True)
