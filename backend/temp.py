from flask import Flask, render_template
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image

model_dir = r'E:\a CS196 group project\neural network\CNN saved models\model 1'
vc = cv2.VideoCapture(1)
ret, captured = vc.read()
#while ret == False:
    #ret, captured = vc.read()
    #print("new attempt!")
print(vc.isOpened())
if ret:
    temp = Image.fromarray(captured, 'RGB')
    resized_img = temp.resize((1024, 1024))
    img_input = np.asarray(resized_img)
    # loads trained model and predict the captured image.
    model = tf.keras.models.load_model(model_dir)
    result = model.predict_classes(np.asarray([img_input]))
    print(result)
else:
    print('failed to capture image!')