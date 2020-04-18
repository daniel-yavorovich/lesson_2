# OS

* Download and install Python 3.7
* Download https://github.com/Daiera/some_Resources/raw/master/dlib-19.17.0-cp37-cp37m-win_amd64.whl into home dir
* Create folder `data` in home dir
* Download and extract content of http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 into data dir
* Open terminal and execute

    C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\python.exe -m venv virtualenv
    pip install dlib-19.17.0-cp37-cp37m-win_amd64.whl
    pip install opencv-python

* Save https://raw.githubusercontent.com/daniel-yavorovich/lesson_2/master/ml.tpl as ml.py and replace env