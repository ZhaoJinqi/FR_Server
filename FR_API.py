#!/usr/bin/python
# Use flask build a API for face detection with opencv
# curl -m 30 -F "file=@test1.jpg;type=image/jpeg" http://192.168.50.192:5001/facedetectapi

from flask import Flask,request,redirect,url_for
# import numpy as np
import os, json
import cv2
from facedetect import facedetect

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/facedetectapi', methods=['POST', 'GET'])
def facedetectapi():
    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'postimg.jpg')
        f.save(upload_path)

        img = cv2.imread(upload_path)  # 读取从终端上传的图像
        result_dict = facedetect(img)  # 对读取到的图像进行人脸检测
        # print(result_Dict)
        # result_trans = [ str(x) for x in result_list ]
        result_json = json.dumps(result_dict)
        return result_json + '\n'
    return 'Error Format'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5001)

