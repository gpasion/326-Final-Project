import unittest
import os 
from input import check_image_existence


class TestImage(unittest.TestCase):
#tests different paths for images
    
    def test_image(self):
        #tests for an existing image
        image_path = "326 project images/food1.jpg"
        result = check_image_existence()
        self.assertTrue(result)

    def test_nonexisting_image(self):
        #tests for a non existing image
        image_path = "326 project images/food1.jpg"
        result = check_image_existence()
        self.assertFalse(result)
    
    def test_subfolder_image(self):
        #tests for an image in a subfolder
        image_path = "326 project images/subfolder/flatlay-of-groceries-on-table.webp"
        result = check_image_existence()
        self.assertTrue(result)
    
    def test_subfolder_nonexisting_image(self):
        #tests for a non existing image in a subfolder
        image_path = "326 project images/subfolder/food.jpg"
        result = check_image_existence()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()