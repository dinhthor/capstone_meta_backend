from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        data = [
            {
                "title": "m1",
                "price": 1,
                "inventory":1,
            },
            {
                "title": "m2",
                "price": 1,
                "inventory":1,
            },
            {
                "title": "m3",
                "price": 1,
                "inventory":1,
            },
        ]
        for d in data:
            MenuItem.objects.create(
                title=d['title'],
                price=d['price'],
                inventory=d['inventory']
            )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)