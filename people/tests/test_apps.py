from django.apps import apps
from django.test import TestCase
from people.apps import PeopleConfig


class TestPeopleConfig(TestCase):

    def test_app(self):
        self.assertEqual('people', PeopleConfig.name)
        self.assertEqual('people', apps.get_app_config('people').name)
