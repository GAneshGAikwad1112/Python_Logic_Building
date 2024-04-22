# Crating a Rest API using flask and Jsonify in python.....

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__=="__main__":
    app.run(debug = True)