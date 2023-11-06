import csv
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
    items = (f'{recipe}: {ingredients}')
    print (items)


# Assuming items list is in the format 'Easy: [...]'
items_list = items.split(": ")[1][1:-1]  # Extracting the list of ingredients from the string

# Extract individual ingredients from the formatted string
ingredient_lines = re.findall(r"'(.*?)'", items_list)

# Dictionary to store item details from CSV file
item_details = {}

# Read data from CSV file and populate item_details dictionary
with open('Food_Database.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        for ingredient in ingredient_lines:
            # Extract item name from the ingredient line
            extracted_item_name = re.match(r'^([\w\s]+)', ingredient).group(1)
            if item_name.lower() == extracted_item_name.lower():
                item_details[item_name] = {
                    'price': float(row['price']),
                    'amount': row['amount'],
                    'url': row['link']
                }

# Print the retrieved item details
for ingredient in ingredient_lines:
    item_name, amount = re.match(r'^([\w\s]+)', ingredient).group(1), re.search(r'\((\d+\s?\w+)\)', ingredient).group(1)
    if item_name in item_details:
        details = item_details[item_name]
        print(f"Item: {item_name}, Amount: {amount}, Price: {details['price']}, URL: {details['url']}")
    else:
        print(f"Item: {item_name}, Amount: {amount}, Price: None, URL: None")
