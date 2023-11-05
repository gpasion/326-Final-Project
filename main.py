from input import *
from RecipeFinder import *
grocery_list = []
while True:
    image_filename = input("Enter the image file name or 'List' to input list as text: ")
    if check_image_existence(image_filename):
        detected_groceries_list = detect_groceries(image_filename)
        print("\nCurrent List of Groceries:")
        for i in detected_groceries_list:
            print("-", i)
        save_list_to_file(detected_groceries_list)
        generate_recipe()
        break
    elif image_filename == "List":
        get_grocery_list(grocery_list)
        generate_recipe()
        break
    elif image_filename == "exit":
        print("Exiting")
        break
    else:
        print("Image doesn't exist.")