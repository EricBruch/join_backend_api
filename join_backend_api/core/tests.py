from rest_framework.test import APITestCase


class BasicTest(APITestCase):
    def test_get_a_board_list(self):
        response = self.client.get('/boards/')
        self.assertEqual(type(response.json()['results']), list)
