import re 
import os

with open("step2output_template.txt" , "r") as file:
    text = file.read()

#this line is importung the text file that lists ingredients"""

#will use regex in the following lines to give recipe details"""

pattern = r' (Recipe Title: ) (.*)'

title = "Recipe for your ingredients"

# updated_text = re.sub( pattern, r'\1\n' + title)
