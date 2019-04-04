"""
this is a program which test the api.
"""

import requests
import json
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
# Notice: You need change the ip address which is your computer own
detect_url = 'http://192.168.50.57:5001/facedetectapi'
# You can change the picture(test1, test2 or your image)
img_path = './test1.jpg'
img = cv2.imread(img_path)
file = {'image':open(img_path, 'rb')}

# receive data from API server
response = requests.post(detect_url, files = file)
result = json.loads(response.text)
print(result)

vis = img.copy()
for index in range(result['faceNum']):
    # x = revfaces['faces'][0]['face{}'.format(index)]['left']
    # y = revfaces['faces'][0]['face{}'.format(index)]['top']
    # w = revfaces['faces'][0]['face{}'.format(index)]['width']
    # h = revfaces['faces'][0]['face{}'.format(index)]['height']
    x = result['faces']['{}'.format(index)][0]
    y = result['faces']['{}'.format(index)][1]
    w = result['faces']['{}'.format(index)][2]
    h = result['faces']['{}'.format(index)][3]
    # draw rectangle
    cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # print index
    cv2.putText(vis, str(index), (x + 5, y - 5), font, 0.75, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('Output', vis)
cv2.waitKey(5000)
