import re
import pandas as pd
import os
import glob


class Recipe:
    def __init__(self, title, cook_time, difficulty, servings, utensils, ingredients, instructions, shopping_list):
        """
        Initialize a Recipe object.

        Parameters:
        - title (str): The title of the recipe.
        - cook_time (int): The cooking time in minutes.
        - difficulty (str): The difficulty level of the recipe.
        - utensils (list): List of strings representing required utensils.
        - ingredients (list): List of strings representing ingredients.
        - instructions (list): List of strings representing cooking instructions.
        - shopping_list (list, optional): List of ShoppingListItem objects for the recipe's shopping list.
        """
        self.title = title
        self.cook_time = cook_time
        self.difficulty = difficulty
        self.servings = servings
        self.utensils = utensils
        self.ingredients = ingredients
        self.instructions = instructions
        self.shopping_list = shopping_list
        self.cost_per_serving = self.calculate_cost_per_serving()

    ### Output, no tests needed
    def __str__(self):
        '''
        Returns a recipe string that includes descriptions regarding the recipe. Description includes cook time, ingredients, time to cook, etc.
        Returns: 
            recipe_str(str) recipe string that includes recipe details
        '''
        recipe_str = f"Recipe Details:\nTitle: {self.title}\nCook Time: {self.cook_time} minutes\nDifficulty: {self.difficulty}\nServings: {self.servings}\nCost per serving: {self.cost_per_serving}\n"
        recipe_str += f"Utensils: {', '.join(self.utensils)}\n"
        recipe_str += f"Ingredients: {', '.join(self.ingredients)}\n"
        recipe_str += "Instructions:\n"
        recipe_str += "\n".join([f" {step}" for step in self.instructions])
        
        if self.shopping_list:
            recipe_str += "Shopping List:\n"
            for item in self.shopping_list:
                recipe_str += f"{item.name}; Price per Unit: ${item.price_per_unit:.2f}; Weight: {item.weight}oz; Cost per Ounce: ${item.cost_per_oz:.2f}; URL: {item.url}" + "\n"

        return recipe_str
    
    #TODO: FOR GABE TEST, need to create a few instances of recipe(manually) and make sure it counts calculate_cost_per_serving properly(the function is run when instance created)
    def calculate_cost_per_serving(self):
        '''
        Itierates through the ingredient list and determines if there is a match within the shopping list.
        Code then calculates cost per serving depending on price for each ingredient

        Returns:
            total_cost(float): Total cost per each serving

        '''
        total_cost = 0
        for ingredient_str in self.ingredients:
            # Extract quantity and name from the ingredient string
            quantity, item_name = ingredient_str.split(' of ')
            quantity = float(quantity.split(' ')[0])
            # Find the corresponding ShoppingListItem object
            matching_item = next((item for item in self.shopping_list if item.name.lower() in item_name.lower()), None)
            if matching_item:
                # Adjust total cost based on quantity and unit in the ingredient list
                total_cost += quantity * matching_item.cost_per_oz

        return total_cost
    
    #TODO: FOR GABE TEST, need to create a few instances of recipe(manually) and make sure it does proper math when update_servings_number is run
    def update_servings_number(self, new_servings_num):
        '''
        Updates the number of servings within the recipe and ingredient amount based on desired amount of servings from user
        Args:
            new_servings_num(int): Number that represents the amount of servings desired for the recipe. 
        '''
        self.servings = new_servings_num
        new_ingredients_list = []
        for ingredient_str in self.ingredients:
            quantity, item_name = ingredient_str.split(' of ')
            new_quantity = float(quantity.split(' ')[0])  * new_servings_num
            new_ingredients_list.append(f"{new_quantity} OZ of {item_name}")
        self.ingredients = new_ingredients_list

class ShoppingListItem:
    """Need to have:
    id: string
    name: string
    price: double, per unit
    weight: double, oz       todo: need to convert lbs to oz if needed
    cost_per_oz: double, dollars
    url: string
    """
    def __init__(self, item_id, name, price_per_unit, weight, url):
        self.id = item_id
        self.name = name
        self.price_per_unit = float(price_per_unit.replace('$', ''))
        self.weight = self.convert_to_oz(weight)
        self.url = url
        self.cost_per_oz = self.calculate_cost_per_oz()
    
    ### Output, no tests needed
    def __str__(self):
      return f"Shopping Item Details:\nID: {self.id}\nName: {self.name}\nPrice per Unit: ${self.price_per_unit:.2f}\nWeight: {self.weight:.2f} oz\nCost per Ounce: ${self.cost_per_oz:.2f}\nURL: {self.url}\n"

    def calculate_cost_per_oz(self):
        '''
        Finds the price per ounce for each item. 
        Returns:
            cost_per_oz(float):float that represents the cost per ounce of the tiem 
        '''
        # Calculate cost per ounce
        cost_per_oz = self.price_per_unit / self.weight
        return round(cost_per_oz, 2)
    
    def convert_to_oz(self, weight_str):
      '''
      Converts the weight of the item to ounces. Item may already be in ounces, 
      which wil not effect the weight. But item may be listed in lbs, which is when the conversion is needed.
      Args:
        weight_str(str): String that states the weight of the item, which can include it's unit of measurment or not
      Returns:
        numeric_value(float): Weight of item in ounces 
      '''
      # Find the index where the numeric part ends
      index = next((i for i, c in enumerate(weight_str) if not c.isdigit() and c != '.'), None)

      # If no unit part found, default to 'oz'
      if index is None:
          numeric_part = weight_str
          unit_part = 'oz'
      else:
          numeric_part = weight_str[:index]
          unit_part = weight_str[index:].lower()

      # Convert the numeric part to a float
      numeric_value = float(numeric_part)

      # Check the unit and convert to ounces if necessary
      if "lb" in unit_part:
          # Convert pounds to ounces
          numeric_value *= 16

      return numeric_value
  
#TODO: ISRAEL TEST, create few lists of ingredienst manually and make sure they parse with csv properly
def create_shopping_list(csv_path, ingredients):
    '''
    Creates a list of items based on the ingredients needed and uses a CSV file to find these ingredients 
    Args:
        csv_path(str): Path to CSV file
        ingredients(list): list that includes the ingredients needed for the recipe
    Returns:
        shopping_list(list): list of product items based off the CSV file. 

    '''
    shopping_list = []
    grocery_df = pd.read_csv(csv_path)
    for ingredient in ingredients:
      item_name = ingredient.split(' of ')[1]
      matching_records = grocery_df[grocery_df['item_name'].str.contains(item_name, case=False)]
      
      if not matching_records.empty:
          grocery_record = matching_records.iloc[0]
          shopping_list_item = ShoppingListItem(grocery_record.item_id, grocery_record.item_name, grocery_record.price, grocery_record.amount, grocery_record.url)
          shopping_list.append(shopping_list_item)
    return shopping_list

#TODO: ISRAEL TEST, use files in folder recipes_for_tests to make sure those parsed as expected
def parse_recipe_from_file(file_path, csv_path):
    '''
    Parses through recipe details from supplied txt file and generates a recipe based on the ingredients provided 
    Args:
        file_path(str): Path to txt file 
        csv_path(str): Path to the CSV file
    Returns:
        recipe_object: Recipe object that contains elements based on the txt file used 
    '''
    with open(file_path, 'r') as file:
        content = file.read()
    # Use regular expressions to find matches
    title_match = re.search(r"Title:\s*(.*)", content)
    cook_time_match = re.search(r"Cook Time:\s*(.*)", content)
    difficulty_match = re.search(r"Difficulty:\s*(.*)", content)
    servings_match = re.search(r"Servings:\s*(.*)", content)
    utensils_match = re.search(r"Kitchen Utensils:\s*([\s\S]*?)(?=Ingredients:)", content)
    ingredients_match = re.search(r"Ingredients:\s*([\s\S]*?)(?=Instructions:)", content)
    instructions_match = re.search(r"Instructions:\s*([\s\S]*)", content)

    # Extract information from matches
    title = title_match.group(1).strip() if title_match else ""
    cook_time = cook_time_match.group(1).strip() if cook_time_match else ""
    difficulty = difficulty_match.group(1).strip() if difficulty_match else ""
    servings = servings_match.group(1).strip() if difficulty_match else ""
    utensils = [line.strip('- ') for line in utensils_match.group(1).strip().split('\n')] if utensils_match else []
    ingredients = [line.strip('- ') for line in ingredients_match.group(1).strip().split('\n')] if ingredients_match else []
    instructions = [line.strip() for line in instructions_match.group(1).strip().split('\n')] if instructions_match else []


    shopping_list = create_shopping_list(csv_path, ingredients)
    recipe_object = Recipe(title, cook_time, difficulty, servings, utensils, ingredients, instructions, shopping_list)

    return recipe_object


def get_dict_of_recepies(folder_path, csv_path):
    '''
    Goes through the recipe text files in the folder 'recipes' and parses through them
    Args:
        folder_path(str): Path to the 'recipes' folder
        csv_path(str): Path to the CSV file
    Returns:
        recipe_objects_dict(dictionary): Returns a dictionary where current index is the key 
    '''
    # Construct the pattern to match text files
    file_pattern = os.path.join(folder_path, "*.txt")

    # Get a list of all text files in the folder
    text_files = glob.glob(file_pattern)

    recipe_objects_dict = {}
    # Process each text file
    for id, file_path in enumerate(text_files, start=1):
        # Instantiate a unique object for each iteration
        recipe_object = parse_recipe_from_file(file_path, csv_path)

        # Store the object in the dictionary with the current index as the key
        recipe_objects_dict[id] = recipe_object
    return recipe_objects_dict