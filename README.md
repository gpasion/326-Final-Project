# 326-Final-Project
pip libs to run<br/>
pandas<br/>
mediapipe<br/>
cv2_plt_imshow<br/>
openai==028<br/>

Also, file constants.py is needed <br/>
api_key = "your openai apikey" <br/>
MODEL_PATH = "input_module/efficientdet_lite2.tflite" <br/>
FOLDER_PATH = "recipes" <br/>
INGREDIENTS_LIST_FILE_NAME = "grocery_list.txt" <br/>
CSV_PATH = "Food_Database.csv" <br/>
IMAGE_FOLDER = "input_image" <br/>
 <br/>
 Known issue: sometimes GPT-4 will generate a file with improper structure or symbols, making regex unable to detect all required segments and crush the app.  <br/>
 While we know how to properly handle  this (improve prompt and re do request if there is an error, unfortunately, we didn't have enough time to implement this) 
