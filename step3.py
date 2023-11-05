#import csv
import re

# Regular expression pattern to match lines starting with a number (indicating quantities)
ingredient_pattern = r'^- (\d+\s?\w+.+)$'

# List of file paths
file_paths = ['recipes/easy_recipe.txt', 'recipes/intermediate_recipe.txt', 'recipes/advanced_recipe.txt']

# Dictionary to store recipe names as keys and corresponding ingredient lists as values
recipes = {}

# Loop through each file path and read its contents
for file_path in file_paths:
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        is_inside_ingredients = False  # Flag to track if inside "Ingredients" section
        ingredient_list = []  # List to store extracted ingredients

        for line in lines:
            # Check if the line matches the updated "Ingredients" pattern
            if re.match(ingredient_pattern, line):
                is_inside_ingredients = True
                ingredient_match = re.match(ingredient_pattern, line)
                ingredient = ingredient_match.group(1)
                ingredient_list.append(ingredient.strip())
            elif is_inside_ingredients and line.strip():
                # Check if the line is not empty and inside "Ingredients" section
                # Add your logic to process ingredients and quantities here, if needed
                pass

        # Extract the recipe name from the file path (assuming the file name is in the format "recipe_name.txt")
        recipe_name = file_path.split('/')[-1].split('_')[0].capitalize()
        recipes[recipe_name] = ingredient_list

# Print the extracted ingredients for each recipe
for recipe, ingredients in recipes.items():
    print(f'{recipe}: {ingredients}')
