import sys
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from django.contrib.postgres import fields

from PIL import Image
from io import BytesIO


class Person(models.Model):
    """Defines the Product Class."""
    name = models.CharField(max_length=100, default='')
    blurb = models.CharField(max_length=254, default='')
    story = models.TextField()
    video = models.URLField()
    portrait = models.ImageField(upload_to='portraits')
    thumb = models.ImageField(upload_to='portraits/thumbs')
    pattern1 = models.ImageField(upload_to='patterns', blank=True, default='')
    pattern1_bg = models.CharField(max_length=7, blank=True, default='')
    pattern1_txt = models.CharField(max_length=7, blank=True, default='')
    tags = fields.ArrayField(models.CharField(max_length=40), size=10)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """ Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/ """

        img = Image.open(self.portrait)
        img_format = img.format.lower()

        # Prevents images from being copied on every save
        # will save a new copy on an upload
        person = Person.objects.get(pk=self.id)
        if (self.portrait.name != person.portrait.name) \
                or (not person):
            # Image is resized
            output_size = (106, 139)
            img = img.resize(size=(output_size))

            # Converts format while in memory
            output = BytesIO()
            img.save(output, format=img_format)
            output.seek(0)

            # Replaces the Imagefield value with the newly converted image
            self.thumb = InMemoryUploadedFile(
                output,
                'ImageField',
                f'{self.portrait.name.split(".")[0]}.{img_format}',
                'image/jpeg', sys.getsizeof(output),
                None)

            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
