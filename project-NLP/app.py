import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
from flask import Flask , request, render_template,url_for
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html')

@app.route('/select',methods=['POST'])
def select():
    return render_template('base.html')


@app.route('/text')
def text():
    return render_template('text.html')


@app.route('/project')
def reviewtext():
    return render_template('reviewtext.html')



@app.route('/page')
def page():
    return render_template('base.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    y_pred=request.form['ms']
    if(y_pred =='true'):
            img_url = url_for('static',filename = 'style/1.jpg')
            topic = "Positive Tweet"
    elif(y_pred =='false'):
            img_url = url_for('static',filename = 'style/2.jpg')
            topic = "Negative Tweet"
    else:
            img_url = url_for('static',filename = 'style/3.jpg')
            print(img_url)
            topic = "Neutral Tweet"
    return render_template('base.html',ypred = topic)
        
if __name__ == '__main__':
    app.run(debug = True, threaded = False)

