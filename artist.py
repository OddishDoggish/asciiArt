import PIL
import numpy as np
import scipy as sp
from scipy.spatial import distance
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def scale_down(image, new_w):

    (orig_w, orig_h) = image.size
    aspect_ratio = orig_h/orig_w
    new_h = round(aspect_ratio * new_w)
    new_image = image.resize((new_h,new_w))

    return new_image


def color_convert(image_array, x, y):
    red = str(int(51 * round(image_array[x, y, 0] / 51)/51))
    grn = str(int(51 * round(image_array[x, y, 1] / 51)/51))
    blu = str(int(51 * round(image_array[x, y, 2] / 51)/51))
    color_string = red + grn + blu

    return color_string


def img_convert(image_array):
    (w, h, colors) = image_array.shape
    color_string = ''
    last_color = ''
    for x in range(0, w-1):
        for y in range(0, h-1):
            new_color = color_convert(image_array, x, y)
            if new_color == last_color:
                color_string = color_string + " "
            else:
                color_string = color_string + "|[" + new_color + " "
            last_color = new_color
        color_string = color_string[0:len(color_string)-1] + "|[" + last_color + "|_|/"
        if len(color_string) > 7700:
            print('\\\\' + color_string)
            color_string = ''
            last_color = ''

    return color_string


# image = Image.open('Osmium3.jpg')
image = Image.open('elf3.jpg')
print('Image opened.')

standard = 40
image_sc = scale_down(image, standard)
image_sc.show()

image_array = np.array(image_sc)

art_string = img_convert(image_array)

#[ print('\\\\' + art_string[i:i+7000]) for i in range(0, len(art_string), 7000) ]
