# Assistive Device for the Blind
Source code for electronic assistive device capable of utilizing open source state of the art Monocular Depth Estimation and Automatic Image Captioning models to assist blind people with indoor and outdoor navigation and scene understanding. The device has 2 functions - navigation mode and generate image caption - which the user can activate using buttons. Further details of the implementation can be found in the ETA repository in my Github profile. 

The navigation mode works as follows: on pressing the assigned button, the device takes a picture through a USB webcam and uses the Depth Estimation model to convert it to a depth map. I then added my own script to convert this depth map into 8 different pitch modulated tones that notify the user of the distance of the  nearest obstacle in 8 different directions.  After this, the device takes another picture and the process is repeated until the user decides to turn off navigation mode.  With my implementation, I managed  to make this entire cycle fast enough while running locally on  the Raspberry Pi 3 Model B.

The generate image caption function is more straightforward. On pressing the assigned button, the device takes a picture and sends it to an API. The API server then uses the Image Captioning model to generate the corresponding caption and send it back to the device. This caption is then converted to speech locally using a text to speech library and played to the user.

To implement the device, I used a Raspberry PI 3 Model B for the device with a custom button circuit and acrylic enclosure, a USB webcam and a pair of earphones. I also set up a REST API with Flask  hosted on a laptop to handle the computationally expensive image captioning model. 

  
## Run locally
1. 



## Tech stack
* Tensorflow
* OpenCV
...
(more docs to follow)

