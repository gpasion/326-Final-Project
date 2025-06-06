import unittest
from recipe_utils import parse_recipe_from_file

class TestParseRecipeFromFile(unittest.TestCase):
    def easy_recipe(self):
        recipe = parse_recipe_from_file('recipes/easy_recipe.txt', 'Food_Database.csv')

        self.assertRegex(recipe.title, r'.+')  # Checking for any non-empty title
        self.assertRegex(recipe.cook_time, r'\d+\s*(?:Minutes|minutes)')
        self.assertIn(recipe.difficulty, ['Easy'])
        self.assertIsInstance(recipe.servings, str)
        self.assertIsInstance(recipe.utensils, list)
        self.assertIsInstance(recipe.ingredients, list)

    def intermediate_recipe(self):
        recipe = parse_recipe_from_file('recipes/intermediate_recipe.txt', 'Food_Database.csv')

        self.assertRegex(recipe.title, r'.+')  # Checking for any non-empty title
        self.assertRegex(recipe.cook_time, r'\d+\s*(?:Minutes|minutes)')
        self.assertIn(recipe.difficulty, ['Intermediate'])
        self.assertIsInstance(recipe.servings, str)
        self.assertIsInstance(recipe.utensils, list)
        self.assertIsInstance(recipe.ingredients, list)

    def advanced_recipe(self):
        recipe = parse_recipe_from_file('recipes/advanced_recipe.txt', 'Food_Database.csv')

        self.assertRegex(recipe.title, r'.+')  # Checking for any non-empty title
        self.assertRegex(recipe.cook_time, r'\d+\s*(?:Minutes|minutes)')
        self.assertIn(recipe.difficulty, ['Advanced'])
        self.assertIsInstance(recipe.servings, str)
        self.assertIsInstance(recipe.utensils, list)
        self.assertIsInstance(recipe.ingredients, list)

if __name__ == '__main__':
    unittest.main()
