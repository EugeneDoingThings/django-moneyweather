from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    def test_view_money(self):
        response = self.client.get('/money/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'RUB')
        self.assertContains(response, 'USD')


    # def test_view_hello_param(self):
    #     response = self.client.get('/hello/', {'name': 'Nikita'})
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'Hello, Nikita!')
