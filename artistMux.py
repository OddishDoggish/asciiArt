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
    aspect_ratio = orig_h / (orig_w * cursor)
    new_h = round(aspect_ratio * new_w)
    new_image = image.resize((new_w, new_h))

    return new_image


def color_convert(image_array, x, y):
    colors = (0, 95, 135, 175, 215, 255)
    red = min(colors, key=lambda n: abs(n - image_array[x, y, 0]))
    grn = min(colors, key=lambda n: abs(n - image_array[x, y, 1]))
    blu = min(colors, key=lambda n: abs(n - image_array[x, y, 2]))
    #    red = str(int(51 * round(image_array[x, y, 0] / 51)/51))
    #    grn = str(int(51 * round(image_array[x, y, 1] / 51)/51))
    #    blu = str(int(51 * round(image_array[x, y, 2] / 51)/51))
    color_string = "%X<" + str(red) + " " + str(grn) + " " + str(blu) + ">"

    return color_string


def img_convert(image_array):
    (w, h, colors) = image_array.shape
    color_string = ''
    last_color = ''
    count = 1
    for x in range(0, w - 1):
        for y in range(0, h - 1):
            new_color = color_convert(image_array, x, y)
            if new_color == last_color:
                color_string = color_string + "%b"
            else:
                color_string = color_string + new_color + "%b"
            last_color = new_color
            """
                count = count + 1
                if count == h:
                    color_string = color_string + "[ansi(/" + new_color + ",space(" + str(count) + "))]"
                    count = 1
            else:
                color_string = color_string + "[ansi(/" + new_color + ",space(" + str(count) + "))]"
                count = 1
            last_color = new_color
            """

       # color_string = color_string + "%R"
        color_string = color_string[0:len(color_string) - 2] + last_color + "%b%Xn%R" + last_color
        if len(color_string) > 15000:
            print('think ' + color_string[0:len(color_string) - (5+len(last_color))])
            color_string = ''

    print('think ' + color_string)

    return color_string


#image = Image.open('Osmium3.jpg')
#image = Image.open('lemons.jpg')
#image = Image.open('puffin.jpg')
#image = Image.open('Eline_Powell_GOT.jpg')
image = Image.open('bikini.jpg')
print('Image opened.')

standard = 80
image_sc = scale_down(image, standard)
image_sc.show()

image_array = np.array(image_sc)

art_string = img_convert(image_array)
