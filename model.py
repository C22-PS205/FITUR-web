import matplotlib
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"""
References : https://github.com/chrispmaag/flask_with_tensorflow_lite/blob/92787720adbb0abbc0477cab6fbcbc5107caac83/inference.py
"""
matplotlib.use('Agg')

def get_category(img):
    img = mpimg.imread(img)
    img = tf.cast(img, tf.float32)
    img = tf.image.resize(img, [224, 224])
    img = np.expand_dims(img, axis=0)

    tflite_model_file = 'Klasifikasi_3_Jenis_Penyu_VGG16Net.tflite'

    with open(tflite_model_file, 'rb') as fid:
        tflite_model = fid.read()

    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    
    prediction = []
    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    prediction.append(interpreter.get_tensor(output_index))

    predicted_label = np.argmax(prediction)
    class_names = ['Chelonia mydas', 'Dermochelis coriaceae', 'Natator depressus']
    
    return class_names[predicted_label]


# def plot_category(img):
def plot_category(img, current_time):
    img = mpimg.imread(img)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    strFile = f'static/images/output_{current_time}.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.savefig(strFile)