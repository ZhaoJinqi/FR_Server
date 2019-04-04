import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def facedetect(image):
    """
    This function is called facedetect.
    It can be used to detect the position of all faces in the image which is detected.
    :param image:
    :return: faces_info
    """
    faces_info = {}  # the Dictionary of information of all faces in the image which is detected
    faces_dict = {}  # the Dictionary of all faces
    # faceRect = {}   # the Dictionary of single face

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces_info['faceNum'] = faces.shape[0]

    for index in range(faces.shape[0]):
        # face_rect = faces[index][0]
        # face_rect = faces[index][1]
        # face_rect = faces[index][2]
        # face_rect = faces[index][3]
        faces_dict[index] = faces[index].tolist()

    faces_info['faces'] = faces_dict
    return faces_info

if __name__ == '__main__':
    img = cv2.imread('test1.jpg')  # Ths is an image for testing
    rec_faces = facedetect(img)
    print(rec_faces)

    vis = img.copy()
    for index in range(rec_faces['faceNum']):
        # x = revfaces['faces'][0]['face{}'.format(index)]['left']
        # y = revfaces['faces'][0]['face{}'.format(index)]['top']
        # w = revfaces['faces'][0]['face{}'.format(index)]['width']
        # h = revfaces['faces'][0]['face{}'.format(index)]['height']
        x = rec_faces['faces'][index][0]
        y = rec_faces['faces'][index][1]
        w = rec_faces['faces'][index][2]
        h = rec_faces['faces'][index][3]
        # draw rectangle
        cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # print index
        cv2.putText(vis, str(index), (x + 5, y - 5), font, 0.75, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Output', vis)
    cv2.waitKey(5000)