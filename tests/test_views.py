from django.views import generic
from django.test import TestCase

class HomeView(generic.TemplateView):

    template_name = 'template/index.html'

class SearchView(generic.TemplateView):

    template_name = 'template/search.html'

class AuthorListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("https://www.google.com/maps/@?api=1&map_action=pano&pano=tu510ie_z4ptBZYo2BGEJg&viewpoint=48.857832%2C2.295226&heading=-45&pitch=38&fov=80")
        self.assertEqual(response.status_code, 200)