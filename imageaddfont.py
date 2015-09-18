# coding: utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
im = Image.open("/users/liweijian/Downloads/1.jpeg")
d = ImageDraw.Draw(im)
fnt = ImageFont.truetype('/Library/Fonts/Mishafi.ttf',20)
d.text((10,10),"5",font=fnt,fill=(255,255,255,128))
im.show()
