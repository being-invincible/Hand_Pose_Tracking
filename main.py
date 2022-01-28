# import the opencv library
import cv2
from cv2 import line

import mediapipe as mp
import time

# define a video capture object
vid_cap = cv2.VideoCapture(0)

# mediapipe's solutuions api
# hand method
mpHands = mp.solutions.hands
hands = mpHands.Hands() 

# draw_utils method for drawing the predictions
mpDraw = mp.solutions.drawing_utils

# time variables
cTime = 0
pTime = 0

while True:
    # Capture the video frame by img frame
    success, img = vid_cap.read()
    # Converting the opencv's GBR to RGB img
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Extracting hand information from hands object
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks) # Check if result returns anything

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # fps = 1/(current time - previous time)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 

    # Display the fps
    # Write some Text
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    topLeftCornerOfText = (10,70)
    fontScale              = 3
    fontColor              = (255,0,255)
    thickness              = 3
    lineType               = 2

    cv2.putText(img, str(int(fps)), topLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

    # Display the resulting frame
    cv2.imshow("Image", img)


    # the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break