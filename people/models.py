import sys
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist
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
    open_graph = models.ImageField(upload_to='portraits/open_graph',
                                   blank=True)
    thumb = models.ImageField(upload_to='portraits/thumbs', blank=True)
    pattern1 = models.ImageField(upload_to='patterns', default='')
    pattern1_bg = models.CharField(max_length=7, blank=True, default='#000000')
    pattern1_txt = models.CharField(max_length=7, blank=True,
                                    default='#ffffff')
    tags = fields.ArrayField(models.CharField(max_length=40), size=10)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """ Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/ """

        # Prevents images from being copied on every save
        # will save a new copy on an upload
        try:
            person = Person.objects.get(pk=self.id)
        except ObjectDoesNotExist:
            person = None

        img = Image.open(self.portrait)
        img_format = img.format.lower()
        if (person and self.portrait.name != person.portrait.name) \
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
