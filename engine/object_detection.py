from flask import Flask, render_template, request
from keras.applications.inception_v3 import *
from keras.preprocessing import image
import tensorflow as tf
import numpy as np
import os
import json

app = Flask(__name__, template_folder=os.path.abspath("../gui/"))

model = InceptionV3(weights='imagenet')
graph = tf.get_default_graph()


def predict(path):
    img = image.load_img(path, target_size=(299, 299))
    xy = image.img_to_array(img)
    xy = np.expand_dims(xy, axis=0)
    xy = preprocess_input(xy)
    global graph
    with graph.as_default():
        preds = model.predict(xy)
    preds = decode_predictions(preds, top=3)[0]
    acc = []
    classes = []
    for x in preds:
        acc.append(x[2])
        classes.append(x[1])
    return acc, classes


@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "GET":
        return render_template("object.html")

    if request.method == "POST":
        path = request.form["path"]

        accuracies, classes = predict(path)

        return render_template("object.html", preds=accuracies,
                               classes=json.dumps(classes), img=path)

app.run()
