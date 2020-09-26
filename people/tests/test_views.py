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
            pattern1=new_photo,
            tags=['this', 'is', 'a', 'tag', 'list'])
        return super().setUp()

    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'people/person_list.html')
        self.assertTemplateUsed(response, 'people/person_detail.html')
        self.assertTemplateUsed(response, 'people/includes/person_box.html')
        self.assertTemplateUsed(response, 'people/includes/detail_modal.html')

        self.assertQuerysetEqual(response.context['people'],
                                 Person.objects.all(),
                                 transform=lambda x: x)
    
    def test_ajax_render_detail(self):
        person = Person.objects.latest('date')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/person/ajax/{person.id}/',
                                   {'item-id': person.id},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'people/includes/detail_modal.html')
        self.assertTemplateUsed(response, 'people/person_detail.html')

