# Hand Pose Tracking

Import the neccesary modules for hand psoe tracking using opencv and Google's mediapipe


```
pip install opencv-python mediapipe

```

Now change directory to where the downloaded main.py file.

Run it and see the magic of hand pose tracking

There are various uses to hand pose tracking like volume control, gesture control (in the field of robotics too), etc.

<img width="708" alt="Result01" src="https://user-images.githubusercontent.com/86947956/151518827-4d71922c-4661-4347-80f8-a08279666443.png">

Title of the Project: #### Cursor Control by Hand Gestures

#### Problem Definition/ Abstract:
World swifts towards technology much faster every day such as AI, VR, etc. The 
results of such development works (like Meta VR World, VR Games – Beat Saber, 
etc.) have already created a lot of hype with the users. This led to the development of 
gadgets which the users can wear to interact with VR. Several products for VR 
interaction have been made worldwide for hands, legs, & body tracking. These devices 
would cost more & would also be bulky to carry around. So, to interact with such great 
VR technologies, computer vision can be used which can take video inputs from the 
webcam. This method will provide an efficient & powerful way to unleash the full 
potential of controlling basic action with just the camera. These basic actions may vary 
from tracking the finger movements to moving the cursor & to do a click when two 
fingers are joined. A more advanced research phase would be to track the whole-body
movements of a human standing in front of the camera and feed them as inputs to the 
VR worlds. This project will serve as a start line for a powerful computer vision use 
case which can be widely implemented in several gesture control applications.

#### Related Work / Existing System:
Prior to the cursor control by hand gestures, VR gadgets such as gloves, kneecaps, 
head band, etc. all are equipped with a pair of motion detector sensors that in turn 
increase the cost of the manufactured product. Also, some of these products seemed
heavy to carry around; few of them were wear & tear. Over the last five years deep 
learning practitioners have researched with tons of GPU to produce state of the art 
detection models. But a detection model can only detect the subject. To bring out more 
functionality, diverse features must be derived based on the application usage. A more 
generalized version of Gesture detection should also be made open source so that 
several other practitioners can get benefited from the feature & to make it a bit more 
generalized.

#### Proposed System:
For a proposed objective, the plan is to produce a platform where the user can interact 
with the computer's cursor using a computer vision technique - "Media pipe”, an 
advanced deep neural network model. This proposed system is considered to have 
strong scope around the Virtual Reality worlds where the computer must track the 
motions of several human joints to bring a better virtual experience using a camera.
Hand Gestures are tracked using Media Pipe to detect hand poses and signs which 
can be correlated towards the cursor movement of the computer. Several Cursor 
operations like clicks, movements, & tapping can be achieved via the computer vision 
model (without the mouse).

References -
1. MediaPipe - https://mediapipe.dev
2. Open Cv - https://opencv.org
