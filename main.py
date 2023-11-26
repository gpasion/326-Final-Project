from input import *
from recipe_utils import *
from constants import *




get_filename_or_list_input(INGREDIENTS_LIST_FILE_NAME)
recipe_objects_dict = get_dict_of_recepies(FOLDER_PATH, CSV_PATH)

for key, recipe in recipe_objects_dict.items():
    print(f"Recipe {key}:\nTitle: {recipe.title}\nTime to cook: {recipe.cook_time}\nDifficulty: {recipe.difficulty}\nUtensils needed: {', '.join(recipe.utensils)}\nCost per serving: {recipe.cost_per_serving}\n")


recipe_choice, num_of_servings = get_recipe_choice_and_serving_num()

print(final_output(recipe_objects_dict, recipe_choice, num_of_servings))