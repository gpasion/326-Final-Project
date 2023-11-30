import unittest
import pandas as pd

class ShoppingListItem:
    def __init__(self, item_id, item_name, price, amount, url):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.amount = amount
        self.url = url

def create_shopping_list(csv_path, ingredients):
    # ... (existing code)
    shopping_list = []
    grocery_df = pd.read_csv(csv_path)
    for ingredient in ingredients:
      item_name = ingredient.split(' of ')[1]
      matching_records = grocery_df[grocery_df['item_name'].str.contains(item_name, case=False)]
      #makes sure matching_records is not empty
      print(f"Matching Records for {ingredient}: {matching_records}")
      
      if not matching_records.empty:
          grocery_record = matching_records.iloc[0]
          shopping_list_item = ShoppingListItem(grocery_record.item_id, grocery_record.item_name, grocery_record.price, grocery_record.amount, grocery_record.url)
          shopping_list.append(shopping_list_item)
    return shopping_list

class TestCreateShoppingList(unittest.TestCase):
    def test_shopping_list_creation(self):
        csv_path = 'Food_Database.csv'

        # Testing ingredient list 
        ingredients = [
            '1 lbs of potatoes',
            '12 oz of asparagus',
            '4 lbs of chicken breast'
        ]

        # Testing CSV file, make sure to avoid any white spaces in list items
        csv_content = {
            'item_id': ['60745', '96253', '981833'],
            'item_name': ['Idaho Potatoes', 'Asparagus', 'Chicken Breast'],
            'price': [3.29, 6.99, 17.27],
            'amount': [5, 28, 5.25],
            'url': ['https://www.bjs.com/product/wellsley-farms-idaho-potatoes-5-lbs/3000000000000483628', 'https://www.bjs.com/product/wellsley-farms-fresh-asparagus-28-oz/3000000000000869706', 'https://www.bjs.com/product/wellsley-farms-no-antibiotics-ever-boneless-skinless-chicken-breast-525-75-lbs/3000000000000848594']
        }
        test_df = pd.DataFrame(csv_content)

        # Mock reads the file
        def mock_csv(path):
            return test_df

        # Replaces the read_csv from create_shopping_list with previously made mock read
        pd.read_csv = mock_csv

        # Call the function to create the shopping list
        shopping_list = create_shopping_list(csv_path, ingredients)

        # Makes sure shopping list is 3 items
        self.assertEqual(len(shopping_list), 3)  # Assuming 3 matching items based on the example ingredients

        # Makes sure each item is found
        self.assertEqual(shopping_list[0].item_id, '60745')
        self.assertEqual(shopping_list[1].item_name, 'Asparagus')
        self.assertAlmostEqual(shopping_list[2].price, 17.27, places=2)  # Using places for float comparison


if __name__ == '__main__':
    unittest.main()
