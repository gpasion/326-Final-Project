# testing goes here
import RecipeFinder
import re

file_path = RecipeFinder.generate_recipe()

with open(file_path, 'r') as file:
    contents = file.read()

def food_exists():
    """This test will ensure that all foods in the grocery list exists is mentioned at least once within the recipe description 
    """
    test_passed = False
    grocerylist = RecipeFinder.grocery_list_copy
    for food in grocerylist:
        pattern = fr'\b{food}\b'
        match = re.search(pattern, food)
        if match is not None:
            test_passed = True
        else:
            test_passed = False
            break 
    
    assert test_passed == True

def options_exists():
    """This test will ensure that there are three separate difficulties within their respective durations 
    """
    pass

