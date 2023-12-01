# app.py
import webbrowser
from flask import Flask, render_template
import turtle
import os
from random import randint
import time

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
