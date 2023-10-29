# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from cv2_plt_imshow import cv2_plt_imshow


model_path = "C:/Users/danyi/repo/final_project_326/efficientdet_lite2.tflite"
IMAGE_FILE = "apple.jpg"

img = cv2.imread(IMAGE_FILE)
cv2_plt_imshow(img)

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.2)
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file(IMAGE_FILE)

# STEP 4: Detect objects in the input image.
detection_result = detector.detect(image)
print(detection_result.detections[0])
for item in detection_result.detections:
    print(f"This is \n{item.categories[0].category_name} and the chance is {round(item.categories[0].score * 100)}%")

