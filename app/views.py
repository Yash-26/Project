from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .facerec.faster_video_stream import stream
from .facerec.click_photos import click
from .facerec.train_faces import trainer
from .models import Employee, Detected
from .forms import EmployeeForm
from face_rec_django.settings import MEDIA_ROOT
import cv2
import pickle
import face_recognition
import datetime
from cachetools import TTLCache
from sklearn.metrics.pairwise import euclidean_distances
import joblib
from joblib import load
from deepface import DeepFace
import threading
import threading
from collections import Counter
import joblib
import serial
import time
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Employee
from django.contrib.auth.models import User
import csv


from collections import Counter
from deepface import DeepFace
from .models import DetectedEmotion, DetectedEmotion1

       
import cv2


import cv2
import numpy as np
from tensorflow.keras.models import model_from_json


import copy
import pygame
import time
import sys
from django.http import JsonResponse




def emotions(request):
    if request.method == 'POST':


        face_classifier = cv2.CascadeClassifier(r"app\facerec\models\haarcascade_frontalface_default.xml")

        model_json_file = "app/facerec/models/model.json"
        model_weights_file = "app/facerec/models/Latest_Model.h5"
        pygame.mixer.init()
        
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            classifier = model_from_json(loaded_model_json)
            classifier.load_weights(model_weights_file)

        cap = cv2.VideoCapture(0)


        while True:

            ret, frame = cap.read()
            img = copy.deepcopy(frame)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                fc = gray[y:y+h, x:x+w]

                roi = cv2.resize(fc, (48,48))
                pred = classifier.predict(roi[np.newaxis, :, :, np.newaxis])
                text_idx=np.argmax(pred)
                text_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
                # Define the mapping of emotions to their respective audio files
                
                if text_idx == 0:
                    text= text_list[0]
                    
                    print('Angry')
                    audio_file = 'app/songs/Enemy.mp3'
                if text_idx == 1:
                    text= text_list[1]
                    print('Disgust')
                elif text_idx == 2:
                    text= text_list[2]
                    print('Fear')
                    audio_file = 'app/songs/Fear.mp3'
                elif text_idx == 3:
                    text= text_list[3]
                    audio_file = 'app/songs/Memories.mp3'
                    print('Happy')
                elif text_idx == 4:
                    text= text_list[4]
                    audio_file = 'app/songs/Neutral.mp3'
                    print('Neutral')
                elif text_idx == 5:
                    text= text_list[5]
                    print('Sad')
                    audio_file = 'app/songs/Sad.mp3'
                elif text_idx == 6:
                    text= text_list[6]
                    print('Surprise')
                if audio_file:
                    pygame.mixer.music.stop()  # Stop current audio
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()
                    
                
                
                cv2.putText(img, text, (x, y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 255), 2)
                img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
                DetectedEmotion1.objects.create(
  
                                            emotion=text,
                                            timestamp=timezone.now()
                                        )
                

            cv2.imshow("frame", img)
            # Control audio with key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('p'):  # Pause
                pygame.mixer.music.pause()
            elif key == ord('r'):  # Resume
                pygame.mixer.music.unpause()
            elif key == ord('s'):  # Stop
                pygame.mixer.music.stop()
                audio_file = None
            elif key == ord('q'):  # Quit
                break

        cap.release()
        cv2.destroyAllWindows()

        return render(request, 'app/emotions.html', {"PREDICTION":cv2.imshow('img', img)})
    
    else:
        return render(request, 'app/emotions.html')



def emotion_data_view(request):
    # Fetch all emotion data from the database
    models = DetectedEmotion1.objects.all()
    return render(request, 'app/emotion_data_view.html', {'models':models})






def landingpage(request):
    return render(request, 'app/landingpage.html')

def index(request):
    return render(request, 'app/test3.html')




def identify(request):
	video_capture = cv2.VideoCapture(0)
	identify_faces(video_capture)
	return HttpResponseRedirect(reverse('index'))


