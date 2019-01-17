from django.db import models

# Create your models here.

class TestText(models.Model):
    tag = models.CharField(max_length=40, null = True, blank=True)
    question = models.TextField(null = True, blank=True)
    correct = models.TextField(null = True, blank=True)
    wrong1 = models.TextField(null = True, blank=True)
    wrong2 = models.TextField(null = True, blank=True)
    jeLegislativa = models.BooleanField(default=True, blank=True)
