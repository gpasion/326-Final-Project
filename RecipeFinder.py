# STEP 2

import openai

api_key = "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"

# grocery list placeholder

grocery_list = ["chicken", "broccoli", "rice"]

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