
'''Importing the Libraries'''

import os
import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.utils import img_to_array

model = load_model('./Model/')

webcam = cv2.VideoCapture(1)
classes = ['gun_found', 'no_gun_found']

while webcam.isOpened():

  # Image processing for gun detection:

  stat,frm = webcam.read()
  x = cv2.resize(frm, (100,100))
  x = x.astype('float')/255
  x = image.img_to_array(x)
  x = np.expand_dims(x, axis=0)

  # Label for the frame
  confidence = model.predict(x)[0]
  i = np.argmax(confidence)
  label = classes[i]
  label = "{}: {:,2f}%".format(label,100*confidence[i])
  
  cv2.putText(frm, label, (0,0), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 1)
  cv2.imshow("Gun Detection", frm)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
webcam.release()
cv2.destroyAllWindows()