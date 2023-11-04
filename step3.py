import csv

# Read input data from a text file
with open('step2_output_step3_input.txt', 'r') as file:
    input_data = {}
    for line in file:
        # Split the line into item name and quantity
        parts = line.strip().rsplit(' ', 1)
        if len(parts) == 2:
            item, quantity = parts
            input_data[item] = quantity

# CSV data (same as provided in the previous code snippet)
csv_data = """
item_id,item_name,price,amount(lbs/oz/ct(count)),link(url)
# ... (your CSV data here)
"""

# Parse CSV data
csv_reader = csv.DictReader(csv_data.strip().splitlines(), delimiter=',')

# Initialize items_data dictionary
items_data = {}

# Populate items_data dictionary from CSV data
for row in csv_reader:
    item_name = row.get('item_name')
    price = row.get('price')
    link = row.get('link(url)')

    # Check if all required fields are present and non-empty
    if item_name and price and link:
        items_data[item_name] = {
            "price": float(price.strip('$')),
            "link": link
        }
    else:
        print(f"Skipping malformed data: {row}")

# Generate output
for item, quantity in input_data.items():
    if item in items_data:
        # Convert quantity to string (assuming it's a measurement value like "4 ounces")
        formatted_quantity = str(quantity)
        price_per_unit = items_data[item]["price"]
        total_price = price_per_unit * float(quantity.split()[0])  # Extract numeric quantity for calculations
        formatted_price = "${:.2f}".format(total_price)
        output = f"Item: {item}, amount: {formatted_quantity}, price: {formatted_price}, link: {items_data[item]['link']}"
        print(output)
    else:
        print(f"Item '{item}' not found in the CSV data.")