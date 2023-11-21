from input import *
from RecipeFinder import *
from RecipeDescription import *
grocery_list = []

FOLDER_PATH = "recipes"
INGREDIENTS_LIST_FILE = "grocery_list.txt"
CSV_PATH = "Food_Database.csv"

while True:
    image_filename = input("Enter the image file name or 'List' to input list as text: ")
    if check_image_existence(image_filename):
        detected_groceries_list = detect_groceries(image_filename)
        print("\nCurrent List of Groceries:")
        for i in detected_groceries_list:
            print("-", i)
        save_list_to_file(detected_groceries_list)
        generate_recipe(INGREDIENTS_LIST_FILE)
        break
    elif image_filename == "List":
        get_grocery_list(grocery_list)
        generate_recipe(INGREDIENTS_LIST_FILE)
        break
    elif image_filename == "exit":
        print("Exiting")
        break
    else:
        print("Image doesn't exist.")


recipe_objects_dict = get_dict_of_recepies(FOLDER_PATH, CSV_PATH)

# DONE: use those objects to display info to user and ask to make a choice. Show cost per serving and ask home nay servings user would like. 

for key, recipe in recipe_objects_dict.items():
    print(f"Recipe {key}:\nTitle: {recipe.title}\nTime to cook: {recipe.cook_time}\nDifficulty: {recipe.difficulty}\nUtensils needed: {', '.join(recipe.utensils)}\nCost per serving: {recipe.cost_per_serving}\n")
recipe_choice = input("Please enter recipe number and press Enter: \n")
num_of_servings = input("Please enter number of servings and press Enter: \n")

print(final_output(recipe_objects_dict, recipe_choice, num_of_servings))