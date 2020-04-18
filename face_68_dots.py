# Импорт необходимых модулей
from imutils.video import VideoStream, FPS
import cv2
import numpy as np
import dlib

# Запуск видеопотока
vs = VideoStream(src=0).start()

# Подключение детектора, настроеного на поиск человеческих лиц
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

while True:

    # Получение изображения из видеопотока
    frame = vs.read()

    # Конвертирование изображения в черно-белое
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц и построение прямоугольного контура
    faces = detector(grayFrame)

    # Обход списка всех лиц попавших на изображение
    for face in faces:

        # Выводим количество лиц на изображении
        cv2.putText(frame, "{} face(s) found".format(len(faces)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),
                    2)

        # Получение координат вершин прямоугольника и его построение на изображении
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)

        # Получение координат контрольных точек и их построение на изображении
        landmarks = predictor(grayFrame, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 3, (19, 190, 209), -1)
            # cv2.putText(frame, str(n), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 2, cv2.LINE_AA)

        # челюсть
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(0, 16)], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], False, (0, 255, 255), lineType=cv2.LINE_4)

        # челюсть
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(27, 31)], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], False, (0, 255, 255), lineType=cv2.LINE_4)

        # бровь 1
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(17, 22)], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255))

        # бровь 2
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(22, 27)], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255))

        # нос
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(31, 36)], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], False, (0, 255, 255))

        # eye1
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(36, 41)], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255))

        # eye2
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(42, 48)], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255))

        # eye2
        pts = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(48, 65)], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255))





    cv2.putText(frame, "Press ESC to close frame", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Вывод преобразованного изображения
    cv2.imshow("Frame", frame)

    # Для выхода из цикла нажать ESC
    key = cv2.waitKey(1)
    if key == 27:
        break
