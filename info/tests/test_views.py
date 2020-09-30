from django.test import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile

from info.models import About, Email


class TestInfoViews(TestCase):
    def setUp(self):
        new_photo = SimpleUploadedFile(name='image.jpg',
                                            content=open(
                                                'media/portraits/image.jpg',
                                                'rb').read())
        About.objects.get_or_create(
            pk=1,
            title='A title',
            content='This is content',
            background=new_photo)
        return super().setUp()

    def test_render_about(self):
        response = self.client.get('/info/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/about.html')
        self.assertTrue(response.context['about_active'])
        about = About.objects.get(pk=1)
        self.assertEqual(str(about), about.title)

    def test_contact_template(self):
        response = self.client.get('/info/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['contact_active'])
        self.assertTemplateUsed('email_form.html')

    def test_email_sent(self):
        self.client.get('/info/contact/')
        self.client.post('/info/contact/',
                         {'email': 'test@test.com',
                          'name': 'a name',
                          'subject': 'subject',
                          'message': 'this is a message'})
        email = Email.objects.latest('date')
        self.assertEqual(email.name, 'a name')
        self.assertEqual(f'{email.email}, {email.subject}', str(email))
