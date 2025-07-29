from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import MenuItem

class MenuItemTests(APITestCase):

    def setUp(self):
        MenuItem.objects.create(title="Test Pizza", price=9.99, inventory=10)

    def test_get_menu_items(self):
        url = '/restaurant/menu-items/'
        response = self.client.get(url, format='json')
        print('Status code:', response.status_code)
        print('Response data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


    def test_create_menu_item(self):
        url = '/restaurant/menu-items/'
        data = {'title': 'New Burger', 'price': '7.99', 'inventory': 15}
        response = self.client.post(url, data, format='json')
        print('POST status:', response.status_code)
        print('POST data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 1)
        new_id = response.data['id']
        item = MenuItem.objects.get(id=new_id)
        self.assertEqual(item.title, 'Test Pizza')
