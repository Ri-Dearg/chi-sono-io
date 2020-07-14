from django.db import models
from django.utils import timezone
from django.contrib.postgres import fields


class Person(models.Model):
    """Defines the Product Class."""
    name = models.CharField(max_length=100, default='')
    blurb = models.CharField(max_length=254, default='')
    story = models.TextField()
    video = models.URLField()
    portrait = models.ImageField(upload_to='portraits')
    tags = fields.ArrayField(models.CharField(max_length=40), size=10)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
