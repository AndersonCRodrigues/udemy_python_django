from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
# Create your tests here.


class RecipeURLSTest(TestCase):
    def test_recipes_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipes_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={
            'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipes_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={
            'id': 1})
        self.assertEqual(url, '/recipes/1/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home'))
        self.assertIs(views.home, view.func)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={
                'category_id': 1}))
        self.assertIs(views.category, view.func)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={
                'id': 1}))
        self.assertIs(views.recipe, view.func)
