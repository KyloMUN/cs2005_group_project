
import os
import shelve
from flask import Flask, request, render_template

app = Flask(__name__)

persist = shelve.open(os.path.realpath('store.dat'), writeback=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def add_note():
    text = request.form['text']

    print(text)
  
    return render_template('index.html')