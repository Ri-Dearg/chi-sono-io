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
    pattern1 = models.ImageField(upload_to='patterns', blank=True, default='')
    pattern1_bg = models.CharField(max_length=7, blank=True, default='')
    pattern1_txt = models.CharField(max_length=7, blank=True, default='')
    pattern2 = models.ImageField(upload_to='patterns', blank=True, default='')
    pattern2_bg = models.CharField(max_length=7, blank=True, default='')
    pattern2_txt = models.CharField(max_length=7, blank=True, default='')
    pattern3 = models.ImageField(upload_to='patterns', blank=True, default='')
    pattern3_bg = models.CharField(max_length=7, blank=True, default='')
    pattern3_txt = models.CharField(max_length=7, blank=True, default='')
    tags = fields.ArrayField(models.CharField(max_length=40), size=10)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
