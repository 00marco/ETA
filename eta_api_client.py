from __future__ import print_function
import requests
import json
import cv2
import tensorflow as tf
import base64

addr = 'http://localhost:4000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('lena.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
image_as_text = base64.b64encode(img_encoded)
# response = requests.post(test_url, data=image_as_text, headers=headers)
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))
