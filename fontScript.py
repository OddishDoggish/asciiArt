import PIL
import numpy as np
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

letter = "A"
fontname = "cour.ttf"

white = (255,255,255)
black = (0,0,0)

foreground = white
background = black

def letterImage(letter, fontname, foreground, background):
    font = ImageFont.truetype(fontname,12)
    img=Image.new("RGB", (8, 14), background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0),letter,foreground,font=font)
    draw = ImageDraw.Draw(img)
#    img.save(letter + "_test.png")
    return img

letterArt = letterImage(letter, fontname, foreground, background)

