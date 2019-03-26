from flask import Flask
import cv2

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/python")
def hello_python():
    return "Hello Python!"

if __name__ == '__main__':
    app.run(host='192.168.50.192')