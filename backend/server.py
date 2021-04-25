import base64
import urllib
from io import BytesIO

from flask import Flask, render_template, jsonify, request
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from binascii import a2b_base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # POST request
    if request.method == 'POST':
        # get the encoded image sent by POST request
        print('Incoming..')
        data = request.form.keys()
        count = 0
        data_url = None
        for x in data:
            data_url = x
        header, encoded = data_url.split(",", 1)
        print(encoded)
        # decode the posted image, not finished
        decoded_img = base64.decodebytes(bytes(encoded + '==', 'utf-8'))
        with open("image.png", "wb") as f:
            f.write(decoded_img)
        return 'OK', 200

    # GET request
    else:
        message = {'greeting': 'Hello from Flask!'}
        return jsonify(message)


@app.route('/my-link/')
# used for testing
def my_link():
    print('I got clicked!')
    model_dir = r'E:\a CS196 group project\neural network\CNN saved models\model 1'
    vc = cv2.VideoCapture(0)
    ret, captured = vc.read()
    if ret:
        temp = Image.fromarray(captured, 'RGB')
        resized_img = temp.resize((1024, 1024))
        img_input = np.asarray(resized_img)
        # loads trained model and predict the captured image.
        model = tf.keras.models.load_model(model_dir)
        result = model.predict_classes(np.asarray([img_input]))
        print(result)
        if result[0] == 1:
            return "incorrectly"
        else:
            return "correctly"
    else:
        print('failed to capture image!')
        return "nothing"


if __name__ == '__main__':
    app.run(debug=True)
