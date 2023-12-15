import unittest
import os 
from input import remove_item

class TestRemoveItem(unittest.TestCase):
#tests to assure different items are removed
    
    def test_item_removal(self):
        given_grocery_list = ["carrots", "celery", "potatoes", "onions", "bell peppers", "salad greens"]
        user_input = "onions"
        result = remove_item(given_grocery_list, user_input)
        self.assertEqual(result, ["carrots", "celery", "potatoes", "bell peppers", "salad greens"])

    def test_nonexistent_item_removal(self):
        given_grocery_list = ["carrots", "celery", "potatoes", "onions", "bell peppers", "salad greens"]
        user_input = "apple"
        result = remove_item(given_grocery_list, user_input)
        self.assertEqual(result, ["carrots", "celery", "potatoes", "onions", "bell peppers", "salad greens"])

if __name__ == 'main':
    unittest.main()
        
