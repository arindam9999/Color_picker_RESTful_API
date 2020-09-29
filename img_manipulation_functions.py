import cv2
import urllib.request
import numpy as np


def hex_color(pixel):
    val1 = pixel % 16
    pixel //= 16
    val2 = pixel % 16
    hex_val1 = hex(val1)
    hex_val2 = hex(val2)
    s = hex_val2[2:]+hex_val1[2:]
    return s


def color(pixel):
    s=""
    for val in reversed(pixel):
        s += hex_color(val)
    return s


def border_color(img):
    SIZE = 128
    img = cv2.resize(img, (SIZE, SIZE))
    color_table = {}
    for pixel in img[1]:
        if color_table.__contains__(color(pixel)):
            color_table[color(pixel)] += 1
        else:
            color_table[color(pixel)] = 1
    for pixel in img[SIZE-2]:
        if color_table.__contains__(color(pixel)):
            color_table[color(pixel)] += 1
        else:
            color_table[color(pixel)] = 1
    max_key = "000000"
    max_value = 0
    for key, value in color_table.items():
        if value > max_value:
            max_key = key
            max_value = value
    return "#0" + max_key


def primary_color(img):
    SIZE = 128
    img = cv2.resize(img, (SIZE, SIZE))
    color_table = {}
    for rows in img:
        for pixel in rows:
            if color_table.__contains__(color(pixel)):
                color_table[color(pixel)] += 1
            else:
                color_table[color(pixel)] = 1
    max_key = "000000"
    max_value = 0
    b_color = border_color(img)
    for key, value in color_table.items():
        if key != b_color[2:] :
            if value > max_value:
                max_key = key
                max_value = value
    return "#0" + max_key


# Driver Code
url = "https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg"
resp = urllib.request.urlopen(url)
img = np.asarray(bytearray(resp.read()), dtype="uint8")
img = cv2.imdecode(img, cv2.IMREAD_COLOR)
i = primary_color(img)
print(i)
i = border_color(img)
print(i)







