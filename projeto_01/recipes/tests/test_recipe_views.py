from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Recipe, Category, User
# Create your tests here.


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home'))
        self.assertIs(views.home, view.func)

    def test_recipe_home_vies_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_vies_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def teste_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='password',
            email='user@email.com',
        )
        Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
            cover='http://a.com'
        )
        response = self.client.get(reverse('recipes:home'))

        result_context = response.context['recipes']
        self.assertEqual(len(result_context), 1)

        result_content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', result_content)
        self.assertIn('10Minutos', result_content)
        self.assertIn('5 Porções', result_content)

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
