import unittest

from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

from menu.forms import MenuForm
from menu.models import Menu, Ingredient, Item


class MenuTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='very_secret'
        )

        ingredient = Ingredient(name='cherry')
        ingredient.save()

        item = Item(
            name='Cherry soda',
            description='',
            chef=cls.user,
            created_date=timezone.now(),
            standard=True
        )
        item.save()
        item.ingredients.add(ingredient)

        menu = Menu(
            season='Fall 2016',
            created_date=timezone.now()
        )
        menu.save()
        menu.items.add(item)

    def test_index_listing(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('menus' in resp.context)

    def test_menu_detail(self):
        menu = Menu.objects.first()
        resp = self.client.get(reverse('menu_detail', kwargs={'pk': menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('menu' in resp.context)

    def test_menu_item_detail(self):
        item = Item.objects.first()
        resp = self.client.get(reverse('item_detail', kwargs={'pk': item.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('item' in resp.context)

    def test_show_create_form(self):
        resp = self.client.get(reverse('menu_new'))
        self.assertTrue(resp.status_code, 200)
        self.assertTrue('form' in resp.context)

    def test_valid_create_form(self):
        form_data = {'season': 'Spring 2016', 'items': [1], 'expiration_date': None}
        form = MenuForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_edit_menu(self):
        menu = Menu.objects.first()
        resp = self.client.get(reverse('menu_edit', kwargs={'pk': menu.pk}))
        self.assertTrue(resp.status_code, 200)
        self.assertTrue('menu' in resp.context)
