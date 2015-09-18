# coding: utf-8
from PIL import Image
img = Image.open("img/1.jpeg")
x,y = img.size
print x,y
img = img.resize((480,480))
img.show()
