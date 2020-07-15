from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from people.models import Person


class TestPeopleViews(TestCase):

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

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'people/person_list.html')
        self.assertTemplateUsed(response, 'people/includes/person_detail.html')
        self.assertTemplateUsed(response, 'people/includes/person_box.html')

        self.assertQuerysetEqual(response.context['people'],
                                 Person.objects.all(),
                                 transform=lambda x: x)
