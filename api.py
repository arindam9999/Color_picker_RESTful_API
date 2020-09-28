from flask import Flask, request
from flask_restful import Api, Resource
import cv2
import os


def color(pixel):
    WHITE =0
    YELLOW=0.6
    LIME=1.2
    AQUA=1.8
    BLUE=2.4
    PINK=3.0
    pixel[0] /= 100
    pixel[1] /= 100
    pixel[2] /= 100
    if pixel[0] < WHITE+0.3 :
        if pixel[1] < 0.5:
            if pixel[2] >.85:
                return 0
            elif pixel[2] > .55:
                return 1
            elif pixel[2]>0.25:
                return 2
            else:
                return 3
        else:
            if pixel[2]>.25:
                return 4
            else:
                return 5
    elif pixel[0] < YELLOW+0.3:
        if pixel[2]>0.25:
            return 6
        else:
            return 7
    elif pixel[0] < LIME+0.3:
        if pixel[2]>0.25:
            return 8
        else:
            return 9
    elif pixel[0] < AQUA+0.3:
        if pixel[2]>0.25:
            return 10
        else:
            return 11
    elif pixel[0] < BLUE+0.3:
        if pixel[2]>0.25:
            return 12
        else:
            return 13
    elif pixel[0] < PINK+0.3:
        if pixel[2]>0.25:
            return 14
        else:
            return 15


def primary_color(img):
    color_code=['white', 'silver', 'gray', 'black', 'red', 'maroon', 'yellow', 'olive', 'lime', 'green', 'aqua', 'teal', 'blue', 'navy', 'pink', 'purple']
    img = cv2.resize(img, (256, 256))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_table = [0 for i in range(0, 16)]
    for rows in img:
        for pixel in rows:
            color_table[color(pixel)] += 1

    maxe = max(color_table)
    i = -1
    while i < len(color_table):
        i+=1
        if color_table[i] == maxe:
            break
            
    # print(color_code[i])
    return color_code[i]


def border_color(img):
    color_code=['white', 'silver', 'gray', 'black', 'red', 'maroon', 'yellow', 'olive', 'lime', 'green', 'aqua', 'teal', 'blue', 'navy', 'pink', 'purple']
    img = cv2.resize(img, (256, 256))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_table = [0 for i in range(0, 16)]
    for pixel in img[0]:
        color_table[color(pixel)] += 1
    for pixel in img[255]:
        color_table[color(pixel)] += 1
    maxe = max(color_table)
    i = -1
    while i < len(color_table):
        i+=1
        if color_table[i] == maxe:
            break
    # print(color_code[i])
    return color_code[i]


UPLOAD_FOLDER = "static/"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ColorPicker(Resource):
    def get(self):
        file = request.files['image']
        filename = file.name
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = cv2.imread(full_filename)
        os.remove(full_filename)
        return {'primary_color':primary_color(img),'border_color':border_color(img)}


api.add_resource(ColorPicker, "/color_picker")

if __name__ == "__main__":
    app.run(debug=True)
