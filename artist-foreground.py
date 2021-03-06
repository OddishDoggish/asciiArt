import numpy as np
from PIL import Image


def scale_down(image, new_w):
    cursor = 2  # approximate ratio of cursor as pixel
    (orig_w, orig_h) = image.size
    aspect_ratio = orig_h / (orig_w * cursor)
    new_h = round(aspect_ratio * new_w)
    new_image = image.resize((new_w, new_h))

    return new_image


def color_convert(image_array, x, y):
    colors = (0, 95, 135, 175, 215, 255)
    red = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 0]))))
    grn = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 1]))))
    blu = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 2]))))
    color_string = red + grn + blu

    return color_string


def img_convert(image_array, art_char):
    (w, h, colors) = image_array.shape
    color_string = ''
    last_color = ''
    for x in range(0, w - 1):
        for y in range(0, h - 1):
            new_color = color_convert(image_array, x, y)
            if new_color != "000":
                marker = art_char
            #               marker = '☆'
            #                marker = "₪"
            else:
                marker = " "
            if new_color == last_color:
                color_string = color_string + marker
            else:
                color_string = color_string + "|" + new_color + marker
            last_color = new_color
        color_string = color_string[0:len(color_string) - 1] + "|" + last_color + "|_|/"
#        if len(color_string) > 7700:
#            print('\\\\' + color_string)
#            color_string = ''
#            last_color = ''
    print('\\\\' + color_string)

    return color_string


image_name: str = 'images/swordAchard.png'
image = Image.open(image_name)
print('Image opened: ' + image_name)

standard = 60
art_char = '@'
image_sc = scale_down(image, standard)
# image_sc.show()

print('Converting for size: ' + str(standard) + ', and character: ' + art_char)

img_array = np.array(image_sc)
art_string = img_convert(img_array, art_char)
