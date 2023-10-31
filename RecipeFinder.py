# STEP 2

import openai
    
def generate_recipe(ingredients):
    """Will take in the ingredients from the ingredients input and return a step by step recipe
    after communicating with the GPT api

    Returns:
      txt: Will have recipe title, cook time, difficulty, kitchen utensils, ingredient list, and instructions
    """
    api_key = "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"

    # ingredient list placeholder

    file_path = "/Users/gpasion/Documents/GitHub/326-Final-Project/step1_output_and_step2_input.txt"

    with open(file_path, 'r') as file:
        contents = file.read()

    grocery_list = contents.split()

    request = f"Based on these ingredient {' '.join(grocery_list)}, create a recipe in the order recipe title, cook time, easy/intermediate/advanced difficulty, kitchen utensils, ingredient list, and step by step instructions"

    openai.api_key = api_key

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = [{"role": "user", "content": request}],
      max_tokens = 2048
    )

    print(completion)
    # return completion
    return completion





# will change this into a method with a return later just experimenting for now

# have id associating with recipe folder (from step 1)