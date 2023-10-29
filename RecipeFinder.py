# STEP 2

import openai

api_key = "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"

# grocery list placeholder

file_path = "/Users/gpasion/Documents/GitHub/326-Final-Project/step1_output_and_step2_input.txt"
grocery_list = []

with open(file_path, 'r') as file:
    for line in file:
        grocery_list.append(line.split())

print(grocery_list)

request = f"Based on these ingredient {', '.join(grocery_list)}, suggest some recipes"

openai.api_key = api_key

response = openai.Completion.create(
    engine = "davinci",
    prompt = request,
    max_tokens = 150
)

recipes = response.choices[0].text

# will change this into a method with a return later just experimenting for now
print(recipes)