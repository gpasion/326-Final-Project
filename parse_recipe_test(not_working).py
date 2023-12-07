import unittest
from unittest.mock import patch, mock_open
from recipe_utils import parse_recipe_from_file

class TestParseRecipeFromFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="Title: Test Recipe\nCook Time: 30 mins\nDifficulty: Easy\nServings: 4\nKitchen Utensils:\n- Pan\n- Spoon\nIngredients:\n- Ingredient 1\n- Ingredient 2\nInstructions:\n1. Step 1\n2. Step 2\n")
    def test_parse_recipe(self, mock_file):
        csv_path = 'Food_Database.csv'

        # Mock create_shopping_list method for simplicity
        def create_shopping_list(csv_path, ingredients):
            # Mock shopping list data
            return ['Ingredient A', 'Ingredient B']

        # Mock the 'create_shopping_list' function
        with patch('recipe_utils.create_shopping_list', side_effect=create_shopping_list):
            recipe = parse_recipe_from_file('temp_test_file.txt', csv_path)

        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.cook_time, '30 mins')
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()