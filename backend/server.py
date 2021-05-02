import base64
import urllib
from io import BytesIO
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from binascii import a2b_base64

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
        # load captured image into CNN model
        model_dir = r'E:\a CS196 group project\neural network\CNN saved models\model 1'
        temp = Image.fromarray(np.asarray(i), 'RGB')
        resized_img = temp.resize((1024, 1024))
        img_input = np.asarray(resized_img)
        # loads trained model and predict the captured image.
        model = tf.keras.models.load_model(model_dir)
        result = model.predict_classes(np.asarray([img_input]))
        classes = ['correctly', 'incorrectly']
        print(result)
        return classes[result[0]], 200
    else:
        return 'Bad Request', 405


if __name__ == '__main__':
    app.run(debug=True)
