import requests


BASE = "http://127.0.0.1:5000/"
files = {'image': open('image.png', 'rb')}

response = requests.get(BASE+"color_picker", files=files)

print(response.json())
