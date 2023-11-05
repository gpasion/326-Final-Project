#import csv
import re

# Regular expression pattern to match lines starting with a number (indicating quantities)
ingredient_pattern = r'^- (\d+\s?\w+.+)$'

# Read input data from a text file with 'latin-1' encoding
with open('recipes/easy_recipe.txt', 'r', encoding='latin-1') as file:
    lines = file.readlines()

ingredient_list = []
is_inside_ingredients = False  # Flag to track if inside "Ingredients" section

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

# Print the extracted ingredients as a list
print(ingredient_list)


'''# Initialize items_data dictionary
items_data = {}

# Read CSV data from a file named 'data.csv' in the current directory
with open('Food_Database.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        item_name = row.get('item_name')
        price = row.get('price')
        amount = row.get('amount(lbs/oz/ct(count))')
        link = row.get('link(url)')

        # Check if all required fields are present and non-empty
        if item_name and price and amount and link:
            items_data[item_name] = {
                "price": float(price.strip('$')),
                "amount": amount,
                "link": link
            }
        else:
            print(f"Skipping malformed data: {row}")

# Generate output
for item, quantity in input_data.items():
    if item in items_data:
        price_per_unit = items_data[item]["price"]
        total_price = price_per_unit * float(quantity.split()[0])  # Extract numeric quantity for calculations
        formatted_price = "${:.2f}".format(total_price)
        output = f"Item: {item}, amount: {quantity}, price: {formatted_price}, link: {items_data[item]['link']}"
        print(output)
    else:
        print(f"Item '{item}' not found in the CSV data.")
        '''