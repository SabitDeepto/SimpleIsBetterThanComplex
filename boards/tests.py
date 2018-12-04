from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import home

class TestHome(TestCase):
	def checkHome(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def resolve_view_for_home_url(self):
		view = resolve("/home")
		self.assertEquals(views.func, home)