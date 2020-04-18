# OS

Open terminal and copy-paste commands

## Core dependences (mac users only)

* Install brew

    brew install python wget cmake
    brew link python

## Set variables

    VIRTUALENV_PATH="/Users/$USER/.virtualenv"
    DATA_DIR="/Users/$USER/.data"
    MODEL_PATH="$DATA_DIR/shape_predictor_68_face_landmarks.dat"
    SITE_PACKAGES="$VIRTUALENV_PATH/lib/python3.7/site-packages"

## Install virtualenv

    python3.7 -m venv $VIRTUALENV_PATH
    source $VIRTUALENV_PATH/bin/activate
    
## Install requirements

    pip install dlib opencv-python
    
## Model
    
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    open shape_predictor_68_face_landmarks.dat.bz2
    mkdir $DATA_DIR
    mv shape_predictor_68_face_landmarks.dat $MODEL_PATH
    
# TouchDesigner

    wget -O - https://raw.githubusercontent.com/daniel-yavorovich/lesson_2/master/ml.tpl | sed "s#<SITE_PACKAGES>#$SITE_PACKAGES#g" | sed "s#<MODEL_PATH>#$MODEL_PATH#g" > ml.py

    