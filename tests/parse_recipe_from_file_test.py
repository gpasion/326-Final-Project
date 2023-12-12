import unittest
from recipe_utils import parse_recipe_from_file

class TestParseRecipeFromFile(unittest.TestCase):
    def test_easy_recipe(self):
        recipe = parse_recipe_from_file('recipes/easy_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Banana-Apple Carrot Smoothie')
        self.assertEqual(recipe.cook_time, '15 minutes')
        self.assertEqual(recipe.difficulty, 'Easy')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, ['Blender', 'Cutting board', 'Knife'])
        self.assertEqual(recipe.ingredients, ['4 OZ of apple', '3.5 OZ of banana', '2 OZ of carrot'])

    def test_intermediate_recipe(self):
        recipe = parse_recipe_from_file('recipes/intermediate_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Apple Banana Carrot Delight')
        self.assertEqual(recipe.cook_time, '50 minutes')
        self.assertEqual(recipe.difficulty, 'Medium')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, ['Cutting board', 'Knife', 'Blender', 'Saucepan', 'Stirring spoon'])
        self.assertEqual(recipe.ingredients, ['10 OZ of apples', '6 OZ of bananas', '4 OZ of carrots'])

    def test_advanced_recipe(self):
        recipe = parse_recipe_from_file('recipes/advanced_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Baked Caramelized Banana-Apple-Carrot Delight')
        self.assertEqual(recipe.cook_time, '95 minutes')
        self.assertEqual(recipe.difficulty, 'Intermediate')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, ['Oven', 'Knife', 'Baking Tray', 'Measuring Cups', 'Peeler'])
        self.assertEqual(recipe.ingredients, ['6 OZ of banana', '6 OZ of apples', '3 OZ of carrots', '1 OZ of sugar (from apple and banana)'])

if __name__ == '__main__':
    unittest.main()
