import numpy as np

SITE_PACKAGES = '/Users/daniel/.virtualenvs/lesson_2/lib/python3.7/site-packages'
MODEL_PATH = '/Users/daniel/PycharmProjects/lessons/lesson_2/data/shape_predictor_68_face_landmarks.dat'
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
