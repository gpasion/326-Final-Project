# STEP 2

import openai
    
def generate_recipe():
    """Will take in the ingredients from the ingredients input and return a step by step recipe
    after communicating with the GPT api

    Returns:
      txt: Will have recipe title, cook time, difficulty, kitchen utensils, ingredient list, and instructions
    """
    api_key = "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"

    # ingredient list placeholder

    input_path = "grocery_list.txt"

    with open(input_path, 'r') as file:
        contents = file.read()

    grocery_list = contents.split()

    options_dict = [("easy", "15-45"), ("intermediate", "45-90"), ("advanced", "90+")]

    for difficulty, time in options_dict:
      request = f"Please use only ingredients:{' '.join(grocery_list)}, create an {difficulty} recipe that takes {time} to cook, the recipe needs to include following segmnets in order title, cook time, difficulty, kitchen utensils, ingredient section should include complete list of ingredients used in oz, and step by step instructions. Please keep an empty line in between of each section."

      openai.api_key = api_key

      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": request}],
        max_tokens = 2048
      )

      recipe_text = completion.choices[0].message['content']

      # Writing the output to a file
      file_name = f"recipes/{difficulty}_recipe.txt"
      with open(file_name, 'w') as file:
          file.write(recipe_text)

      print(f"Recipe generated for {difficulty}. Check {file_name} for the recipe.")



# will change this into a method with a return later just experimenting for now
