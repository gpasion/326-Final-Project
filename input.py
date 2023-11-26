import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from cv2_plt_imshow import cv2_plt_imshow
from PIL import Image
import openai
from constants import *
"""
Model can work with this:
banana
apple
orange
broccoli
carrot
"""


### Input function, no tests needed
def get_recipe_choice_and_serving_num():
    """Asks the user to choose between 3 different recipes and how many servings they would like to make

    Returns:
        recipe_choice (int): returns the user's choice of recipe quantity
        num_of_servings (int): returns the user's choice of serving quantity

    Side Effects:
        Will change the recipe_choice or num_of_servings based on user input
        Prints the num_of_servings and num of recipe_choice
    """
    while True:
        recipe_choice = input("Please enter recipe number (1-3) and press Enter: ")
        # Check if recipe_choice is a valid integer between 1 and 3
        if recipe_choice.isdigit() and 1 <= int(recipe_choice) <= 3:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

    while True:
        num_of_servings = input("Please enter number of servings and press Enter: ")

        # Check if num_of_servings is an int between 1 and 10(reasonable num of servings in my opinion)
        if num_of_servings.isdigit() and 1 <= int(num_of_servings) <= 10:
            break
        else:
            # If num_of_servings is not reasonable
            if int(num_of_servings) > 10:
                confirmation = input("Are you sure you need that many servings? (yes/no): ")
                if confirmation.lower() in ["yes"]:
                    break
                elif confirmation.lower() in ["no"]:
                    continue
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("Invalid input. Please enter a number of servings you would like.")
        print(recipe_choice)
        print(num_of_servings)
    
    return recipe_choice, num_of_servings

### Input function, no tests needed
def get_filename_or_list_input(ingredients_list_file_name):
    """Takes in an image file and uses the detect_groceries to translate the images into a text list of groceries
    Creates a grocery list based on the text list of groceries (directly starts the list of groceries if the input is a text list)

    Args:
        ingredients_list_file_name (str): file name for the ingredient list

    Side Effects:
        image_filename: takes in user input for either an image file or text input for a list
        other functions used
            check_image_existence(): ensures that the user input file exists
            detech_groceries(): function to return a list of detected food objects
            save_list_to_file(): writes the list into a file called grocery_list.txt
            generate_recipe(): creates a 3 recipes on 3 different difficulties
    """
    while True:
        image_filename = input("Enter the image file name or 'List' to input list as text: ")
        if check_image_existence(image_filename):
            detected_groceries_list = detect_groceries(image_filename)
            print("\nCurrent List of Groceries:")
            for i in detected_groceries_list:
                print("-", i)
            save_list_to_file(detected_groceries_list)
            generate_recipe(ingredients_list_file_name)
            break
        elif image_filename.lower() == "list":
            grocery_list = []
            get_grocery_list(grocery_list)
            generate_recipe(ingredients_list_file_name)
            break
        elif image_filename.lower() == "exit":
            print("Exiting")
            break
        else:
            print("Image doesn't exist.")

#TODO: DANYIL, TEST, check if output files have needed structure(contain all required segments in right format). Technically test for parse_recipe_from_file will handle this
#TODO: Create some files in folder recipes_for_tests to test stuff
def generate_recipe(input_path):
    """Will take in the ingredients from the ingredients input and return a step by step recipe
    after communicating with the GPT api

    Returns:
      txt: Will have recipe title, cook time, difficulty, kitchen utensils, ingredient list, and instructions
    """

    # ingredient list placeholder

    with open(input_path, 'r') as file:
        contents = file.read()

    grocery_list = contents.split()

    options_dict = [("easy", "15-45"), ("intermediate", "45-90"), ("advanced", "90+")]

    for difficulty, time in options_dict:
      request = f"""Please use only ingredients:{' '.join(grocery_list)}, create an {difficulty} recipe that takes {time} to cook, 
      the recipe needs to include following segmnets in order title, cook time, difficulty, 
      servings(please use 1 serving as default), kitchen utensils(please use hyphen), 
      ingredient section should include complete list of ingredients used in oz and have format '- <weight in oz as a number> OZ of <ingridient name>', 
      and step by step instructions.
      Please keep an empty line in between of each section."""

      openai.api_key = api_key

      completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [{"role": "user", "content": request}],
        max_tokens = 2048
      )

      recipe_text = completion.choices[0].message['content']

      # Writing the output to a file
      file_name = f"recipes/{difficulty}_recipe.txt"
      with open(file_name, 'w') as file:
          file.write(recipe_text)

      print(f"Recipe generated for {difficulty}. Check {file_name} for the recipe.")

#TODO:DANYIL, TEST, check if images detect right groceries(they won't, but it's fine)
def detect_groceries(image_filename):
    """Takes in user inputted file name to detect and food items in the image

    Args:
        image_filename (str): takes in an image filename by the user

    Returns:
        detechted_objects (list): Returns a list of the detected food items in the image

    Side Effects:
        detector: the detector object to translate image to text
        image: loads the input image
        detection_result: found items from the image
        detected_objects: list made from the detection_result
    """
    img = cv2.imread(image_filename)
    cv2_plt_imshow(img)

    # STEP 2: Create an ObjectDetector object.
    base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                        score_threshold=0.2)
    detector = vision.ObjectDetector.create_from_options(options)

    # STEP 3: Load the input image.
    image = mp.Image.create_from_file(image_filename)

    # STEP 4: Detect objects in the input image.
    detection_result = detector.detect(image)
    detected_objects = []

    for item in detection_result.detections:
        object_name = item.categories[0].category_name
        detected_objects.append(object_name)
    return detected_objects

#TODO: JOELLE TEST, techincally we just need to provide few paths where images exist/don't and make sure it can find images located withing subfolders
def check_image_existence(filename):
    """Attempts to open the filename, if it does not open throws an exception and returns false

    Args: 
        filename (str): filename in question to see if it exists

    Returns:
        Boolean (true/false): returns true if image exists and false otherwise

    Raises: 
        FileNotFoundError: thrown when the file does not exist or is not found

    Side Effects:
        prints image opened if Image.open() worked
    """
    try:
        img = Image.open(filename)
        print("Image opened")
        return True
    except FileNotFoundError:
        return False

### Input function, no tests needed
def get_grocery_list(grocery_list):
    """Used for text input of grovery list and saves the grovery list to a file

    Args:
        grocery_list (list): empty list of groceries that appends user inputted list

    Side Effects:
        Continues to prompt user to add groveries until done is stated
        Prints the groceryl ist after every update
        Functions used
            remove_items(): takes in user input of a specific item in list, finds it and matches it to an item in the list and removes it
            save_list_to_file(): saves the grocery list to a text file after prompt loop is terminated
    """
    print("Enter 'Done' when you finish entering the groceries.")
    while True:
        item = input("Enter a grocery item, enter 'Remove' to remove item from list or type 'Done' when done entering items: ").strip()
        if item.lower() == 'done':
            break
        if item.lower() == "remove":
            grocery_list = remove_item(grocery_list)
        grocery_list.append(item.lower())
        print("\nCurrent List of Groceries:")
        for i in grocery_list:
            print("-", i)
    save_list_to_file(grocery_list)

#TODO: NOT SURE, Input and saves file, no tests needed???
def save_list_to_file(grocery_list):
    """Saves the inputted grocery list as a text file and asks the user for confirmation to save

    Args:
        grocery_list (list): string list of grocery items

    Side Effects:
        creates confirmed (boolean) and loops while it is false
        if y is inputted, it will write the grocery list to a txt file and end the loop
        prints list saved as {file_name}
        if n inputted, it will print list is not saved
    """
    confirmed = False
    while not confirmed:
        confirm = input("Do you want to save the list to a file? (y/n): ").lower()
        if confirm == 'y':
            file_name = "grocery_list.txt"
            with open(file_name, 'w') as file:
                file.write("\n".join(grocery_list))
            print("List saved as", file_name)
            confirmed = True
        elif confirm == 'n':
            print("List not saved. You can modify the list.")
            get_grocery_list(grocery_list)
            break
        elif confirm == 'exit':
            confirmed = True
            break
        else:
            print("Invalid input. Please enter 'y' to confirm or 'n' to re-enter the list or 'exit' to exit the application.")

#TODO: JOELLE TEST, provide different lists as input and make sure it always removes proper item from the list
def remove_item(grocery_list):
    """Method responsible for item list removal updates by prompting user for the item to be removed

    Args:
        grocery_list (list): list of the groceries as a string
    
    Returns:
        grocery_list (list): updated list of groceries

    Side Effects:
        prints the user input for removal
    """
    for i in grocery_list:
        print("-", i)
    item_to_remove = input("Please enter item to remove: ")
    grocery_list.remove(item_to_remove.lower())
    return grocery_list

### Output function, no tests needed
def final_output(recipe_objects_dict, recipe_choice, num_of_servings):
    """Method for the final output of the chosen recipe

    Args:
        recipe_object_dict (dict): gets dict of folder_path and csv_path of grocery database
        recipe_choice (int): recipe choice based on difficult represented as an integer
        num_of_servings (int): number of servings for the recipe represented as an integer

    Returns:
        recipe_str (str): The entire recipe including title, cook time, difficulty, servings, cost per serving, total cost ingredients, instructions, and shopping list
    """
    chosen_recipe = recipe_objects_dict[int(recipe_choice)]
    chosen_recipe.update_servings_number(int(num_of_servings))
    recipe_str = f"\n\nRecipe Details:\nTitle: {chosen_recipe.title}\nCook Time: {chosen_recipe.cook_time} minutes\nDifficulty: {chosen_recipe.difficulty}\nServings: {chosen_recipe.servings}\nCost per serving: {chosen_recipe.cost_per_serving}\nTotal cost: ${f'{chosen_recipe.cost_per_serving * chosen_recipe.servings:.2f}'}\n"
    recipe_str += f"Utensils: {', '.join(chosen_recipe.utensils)}\n"
    recipe_str += f"Ingredients: {', '.join(chosen_recipe.ingredients)}\n"
    recipe_str += "Instructions:\n"
    recipe_str += "\n".join([f" {step}" for step in chosen_recipe.instructions])
            
    if chosen_recipe.shopping_list:
        recipe_str += "\n\nShopping List:\n"
        for item in chosen_recipe.shopping_list:
            recipe_str += f"{item.name}; Price per Unit: ${item.price_per_unit:.2f}; Weight: {item.weight}oz; Cost per Ounce: ${item.cost_per_oz:.2f}; URL: {item.url}" + "\n"
    return recipe_str