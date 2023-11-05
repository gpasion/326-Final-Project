# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from cv2_plt_imshow import cv2_plt_imshow
from PIL import Image
import os
"""
Model can work with this:
banana
apple
orange
broccoli
carrot
"""

model_path = "input_module/efficientdet_lite2.tflite"
IMAGE_FILE = "input_image/1.jpeg"

def detect_groceries(image_filename):
    img = cv2.imread(image_filename)
    cv2_plt_imshow(img)

    # STEP 2: Create an ObjectDetector object.
    base_options = python.BaseOptions(model_asset_path=model_path)
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

# Function to check if the image exists
def check_image_existence(filename):
    try:
        img = Image.open(filename)
        print("Image opened")
        return True
    except FileNotFoundError:
        return False

# Function to get the list of groceries
def get_grocery_list(grocery_list):
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

# Function to save the grocery list to a text file
def save_list_to_file(grocery_list):
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

def remove_item(grocery_list):
    for i in grocery_list:
        print("-", i)
    item_to_remove = input("Please enter item to remove: ")
    grocery_list.remove(item_to_remove.lower())
    return grocery_list