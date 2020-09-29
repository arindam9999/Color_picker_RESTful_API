import requests
import base64


BASE = "http://127.0.0.1:5000/color_picker/"
urls = [
    "https://storage.googleapis.com/bizupimg/profile_photo/IMG_20200917_190810.jpg",
    "https://storage.googleapis.com/bizupimg/profile_photo/Screenshot%202020-08-16%20at%205.02.30%20PM%20-%20Nikunj%20Daruka.png",
    "https://storage.googleapis.com/bizupimg/profile_photo/DigiKarobar-black.jpeg",
    "https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg"
]
i = 1
f = open("test_outputs.md", "w")
for url in urls:
    message_bytes = url.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_url = base64_bytes.decode('ascii')
    response = requests.get(BASE + base64_url)
    print(i, ":", end=" ", file=f)
    print(response.json(), file=f)
    i += 1
