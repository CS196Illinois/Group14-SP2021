import base64
import urllib
from io import BytesIO
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request
import tensorflow as tf
import numpy as np
from PIL import Image
from binascii import a2b_base64
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.form.get("photo")
        print(request)
        return 'OK', 200


@app.route('/capture', methods=['POST'])
def capture():
    # POST request
    if request.method == 'POST':
        # get the encoded image sent by POST request
        print('Incoming..')
        data = request.form.keys()
        data_url = None
        for x in data:
            data_url = x
        # preprocess encoded string so that python can decode it correctly
        header, encoded = data_url.split(",", 1)
        another = encoded.replace(' ', '+')
        # decode the posted image
        decoded_img = base64.decodebytes(bytes(another, 'utf-8') + b'===')
        # create an Image instance based on decoded image
        i = Image.open(BytesIO(decoded_img))
        i.convert("RGB").save("123.jpg")
        # load captured image into CNN model
        model_dir = r'D:\CS196 group project\128x128'
        resized_img = i.resize((128, 128)).convert("RGB")
        resized_img.convert("RGB").save("test.jpg")
        img_input = np.asarray(resized_img)
        # loads trained model and predict the captured image.
        model = tf.keras.models.load_model(model_dir)
        result = model.predict(np.asarray([img_input]))
        print(result)
        if result[0][0] > result[0][1]:
            return "You are wearing a mask correctly", 200
        else:
            return "You are wearing a mask incorrectly", 200
    else:
        return 'Bad Request', 405


if __name__ == '__main__':
    app.run(debug=True)
