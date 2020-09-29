import PIL
import numpy as np
import scipy as sp
from scipy.spatial import distance
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def scale_down(image, new_w):
    cursor = 2  # approximate ratio of cursor as pixel
    (orig_w, orig_h) = image.size
    aspect_ratio = orig_h/(orig_w * cursor)
    new_h = round(aspect_ratio * new_w)
    new_image = image.resize((new_w, new_h))

    return new_image


def color_convert(image_array, x, y):
    colors = (0, 95, 135, 175, 215, 255)
    red = colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 0])))*36
    grn = colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 1])))*6
    blu = colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 2])))
#    red = str(int(51 * round(image_array[x, y, 0] / 51)/51))
#    grn = str(int(51 * round(image_array[x, y, 1] / 51)/51))
#    blu = str(int(51 * round(image_array[x, y, 2] / 51)/51))
    color_string = str(red + grn + blu + 16)

    return color_string


def img_convert(image_array):
    (w, h, colors) = image_array.shape
    color_string = ''
    last_color = ''
    flag = 0
    for x in range(0, w-1):
        for y in range(0, h-1):
            new_color = color_convert(image_array, x, y)
            if new_color == last_color:
                color_string = color_string + " "
            else:
                color_string = color_string + "%X" + new_color + " "
            last_color = new_color
        color_string = color_string[0:len(color_string)-1] + "%X" + last_color + " %xn%r%X" + last_color
    print('think ' + color_string)

    return color_string


# image = Image.open('Osmium3.jpg')
image = Image.open('cake.jpg')
print('Image opened.')

standard = 80
image_sc = scale_down(image, standard)
image_sc.show()

image_array = np.array(image_sc)

art_string = img_convert(image_array)

