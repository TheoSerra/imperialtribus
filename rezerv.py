#!/usr/bin/python
from flask import FLask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
