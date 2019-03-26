
import cv2
import matplotlib.pyplot as plt
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
img = cv2.imread('demo.jpg') # 此处为测试图

facesInfo = {}
faceDict = {}   #图像中所有人脸的字典
# faceRect = {}   #图像中单一人脸字典

def facedetect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    facesInfo['faceNum'] = faces.shape[0]

    for index in range(faces.shape[0]):
        faceDict['left'] = faces[index][0]
        faceDict['top'] = faces[index][1]
        faceDict['width'] = faces[index][2]
        faceDict['height'] = faces[index][3]
        facesInfo[index] = faceDict
    return facesInfo

if __name__ == '__main__':
    revfaces = facedetect(img)
    print(revfaces)
    # vis = img.copy()

    # for index in range(revfaces['faceNum']):
    #     x = revfaces['faces'][0]['face{}'.format(index)]['left']
    #     y = revfaces['faces'][0]['face{}'.format(index)]['top']
    #     w = revfaces['faces'][0]['face{}'.format(index)]['width']
    #     h = revfaces['faces'][0]['face{}'.format(index)]['height']
    #     # draw rectangle
    #     cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     # draw index
    #     cv2.putText(vis, str(index), (x + 5, y - 5), font, 0.75, (0, 255, 0), 2, cv2.LINE_AA)
    #     # roi_gray = gray[y:y+h, x:x+w]
    #     # roi_color = img[y:y + h, x:x + w]
    # cv2.imshow('hello', vis)
    # cv2.waitKey(5000)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.figure(dpi=150)
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()