from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from people.models import Person


class TestPersonModel(TestCase):

    def setUp(self):
        new_photo = SimpleUploadedFile(name='image.jpg',
                                            content=open(
                                                'media/portraits/image.jpg',
                                                'rb').read())
        Person.objects.get_or_create(
            name='A Person',
            blurb='This is a blurb',
            story='This is the story they are telling',
            video='https://www.youtube.com/watch?v=9xwazD5SyVg',
            portrait=new_photo,
            tags=['this', 'is', 'a', 'tag', 'list'])
        return super().setUp()

    def test_str(self):
        person = Person.objects.latest('date')
        self.assertEqual(str(person), 'A Person')
