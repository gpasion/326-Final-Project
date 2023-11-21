import os
import glob
from RecipeFinder import *

def get_dict_of_recepies(folder_path, csv_path):
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


def final_output(recipe_objects_dict, recipe_choice, num_of_servings):
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