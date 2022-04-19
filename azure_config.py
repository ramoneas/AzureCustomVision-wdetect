import os
from dotenv import load_dotenv

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

import numpy as np

load_dotenv()
cv_key = os.getenv('cv_key')
project_id = os.getenv('project_id')
model_name = os.getenv('model_name')
cv_endpoint = os.getenv('cv_endpoint')
test_img_file = os.getenv('test_img_file') 


def azure_object_detection():
    #Save all the objects found
    objects = []
    
    # Load a test image and get its dimensions
    test_img = Image.open(test_img_file)
    test_img_h, test_img_w, test_img_ch = np.array(test_img).shape

# Get a prediction client for the object detection model
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": cv_key})
    predictor = CustomVisionPredictionClient(endpoint=cv_endpoint, credentials=credentials)

    print('\nDetecting objects in {} using model {} in project {}...'.format(test_img_file, model_name, project_id))

# Detect objects in the test image
    with open(test_img_file, mode="rb") as test_data:
        results = predictor.detect_image(project_id, model_name, test_data)


# Create a figure to display the results
    fig = plt.figure(figsize=(8, 8))
    plt.axis('off')

# Display the image with boxes around each detected object
    draw = ImageDraw.Draw(test_img)
    line_width = int(np.array(test_img).shape[1]/100)
    object_colors = {
    "subfusil": "red",
    "grenade": "yellow",
    "pistol" : "brown",
    "machinegun" : "blue",
    "revolver": "lightgreen"
    }
    for prediction in results.predictions:
        color = 'white' # default for 'other' object tags
        if (prediction.probability*100) > 50:
            print("\nResults: ", prediction.tag_name)
            objects.append(prediction.tag_name)#ENUMERATE THE OBJECTS 
            if prediction.tag_name in object_colors:
                color = object_colors[prediction.tag_name]
            left = prediction.bounding_box.left * test_img_w 
            top = prediction.bounding_box.top * test_img_h 
            height = prediction.bounding_box.height * test_img_h
            width =  prediction.bounding_box.width * test_img_w
            points = ((left,top), (left+width,top), (left+width,top+height), (left,top+height),(left,top))
            draw.line(points, fill=color, width=line_width)
            plt.annotate(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100),(left,top), backgroundcolor=color)
    test_img.save('object_detection_img.jpg')
    plt.imshow(test_img)
    plt.show()
    
    return objects



