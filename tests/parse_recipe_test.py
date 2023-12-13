import unittest
from recipe_utils import parse_recipe_from_file

class TestParseRecipeFromFile(unittest.TestCase):
    def test_quick_and_savory_recipe(self):
        recipe = parse_recipe_from_file('recipes/easy_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Quick and Savory Pork Ribs with Vegetables and Rice')
        self.assertEqual(recipe.cook_time, '45 Minutes')
        self.assertEqual(recipe.difficulty, 'Easy')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, [
            'Knife',
            'Cutting Board',
            'Saucepan',
            'Frying Pan',
            'Stirring Spoon',
            'Measuring Spoons',
            'Measuring Cups'
        ])
        self.assertEqual(recipe.ingredients, [
            '8 OZ of Pork Ribs',
            '2 OZ of Potatoes',
            '2 OZ of Carrots',
            '1 OZ of Bell Pepper',
            '3 OZ of Rice',
            '2 OZ of Sour Cream'
        ])

    def test_roasted_recipe(self):
        recipe = parse_recipe_from_file('recipes/intermediate_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Roasted Pork Ribs with Vegetables and Creamy Rice')
        self.assertEqual(recipe.cook_time, '75 minutes')
        self.assertEqual(recipe.difficulty, 'Intermediate')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, [
            'Oven',
            'Oven tray',
            'Frying pan',
            'Pot',
            'Cutting board',
            'Knife',
            'Spoon'
        ])
        self.assertEqual(recipe.ingredients, [
            '10 OZ of pork ribs',
            '4 OZ of potatoes',
            '2 OZ of carrots',
            '2 OZ of bell pepper',
            '4 OZ of rice',
            '2 OZ of sour cream'
        ])

    def test_slow_cooked_recipe(self):
        recipe = parse_recipe_from_file('recipes/advanced_recipe.txt', 'Food_Database.csv')

        self.assertEqual(recipe.title, 'Slow-Cooked Pork Ribs with Potatoes, Carrots, Bell Pepper and Creamy Rice')
        self.assertEqual(recipe.cook_time, '90+ minutes')
        self.assertEqual(recipe.difficulty, 'Advanced')
        self.assertEqual(recipe.servings, '1')
        self.assertEqual(recipe.utensils, [
            'slow cooker',
            'knife',
            'cutting board',
            'measuring spoons',
            'measuring cups',
            'stovetop pot'
        ])
        self.assertEqual(recipe.ingredients, [
            '16 OZ of pork ribs',
            '8 OZ of potatoes',
            '4 OZ of carrots',
            '4 OZ of bell pepper',
            '2 OZ of rice',
            '1 OZ of sour cream'
        ])

if __name__ == '__main__':
    unittest.main()
