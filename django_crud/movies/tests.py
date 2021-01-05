from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Movie
# Create your tests here.
class movies_crud_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'admin',
            email = 'admin@ahmad.com',
            password = '123456admin'
        )
        self.movie = Movie.objects.create(
            title = 'Joudi',
            director=self.user,
            rate = 10,
            description = 'a movie'
        )

    def test_homepage_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_details_status(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_add_status(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_update_status(self):
        response = self.client.get(reverse('update', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_delete_status(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)


    def test_fields_content(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertContains(response, 'Joudi')
        self.assertContains(response, 'admin')
        self.assertContains(response, 10)
        self.assertContains(response, 'a movie')

    def test_update(self):
        response = self.client.post(reverse('update', args='1'), {
            'title': 'sondos',
        })
        self.assertContains(response, 'sondos')
        self.assertNotContains(response, 'Joudi')
    
    def test_delete(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertNotContains(response, 'sondos')

        
