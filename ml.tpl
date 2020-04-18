import numpy as np

SITE_PACKAGES = '<SITE_PACKAGES>'
MODEL_PATH = '<MODEL_PATH>'
OP_SRC_NAME = 'null1'
OP_TABLE_NAME = 'table1'
import sys

sys.path.append(SITE_PACKAGES)
import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(MODEL_PATH)


def onValueChange(channel, sampleIndex, val, prev):
    data = op(OP_SRC_NAME).numpyArray()

    data = 255 * data
    img = data.astype(np.uint8)

    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # resize image
    scale_percent = 40  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    grayFrame = cv2.resize(grayFrame, dim, interpolation=cv2.INTER_AREA)

    faces = detector(grayFrame)
    dots = []
    for face in faces:
        landmarks = predictor(grayFrame, face)
        for n in range(0, 68):
            dots.append([landmarks.part(n).x, landmarks.part(n).y])

    t = op(OP_TABLE_NAME)
    for idx, dot in enumerate(dots):
        t[idx, 0] = dot[0]
        t[idx, 1] = dot[1]
