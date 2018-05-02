from tensorflow.contrib.keras.python.keras.preprocessing import image
from tensorflow.contrib.keras.python.keras.applications.inception_v3 import *
import numpy as np
import os
import sys
from flask import Flask, render_template, request
import json

app = Flask(__name__)

model = InceptionV3(weights='imagenet')


@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "GET":
        return render_template("object.html")

    if request.method == "POST":
        path = request.form["path"]
        img = image.load_img(path, target_size=(299, 299))

        xy = image.img_to_array(img)
        xy = np.expand_dims(xy, axis=0)
        xy = preprocess_input(xy)

        preds = model.predict(xy)
        preds = decode_predictions(preds, top=3)[0]
        acc = []
        classes = []
        for x in preds:
            acc.append(x[2])
            classes.append(x[1])
        return render_template("object.html", preds=acc, classes=json.dumps(classes), img=path)


app.run()
