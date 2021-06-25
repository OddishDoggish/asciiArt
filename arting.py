import numpy as np
import sys
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
    grays = (0, 8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198, 208, 218, 228, 238)
    if abs((image_array[x, y, 0]/100 - image_array[x, y, 1]/100 - image_array[x, y, 2]/100)*100) < 6:
        color_string = "=" + chr(97 + grays.index(min(grays, key=lambda n: abs(n-image_array[x, y, 1]))))
    else:
        red = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 0]))))
        grn = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 1]))))
        blu = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 2]))))
        color_string = red + grn + blu
    if color_string == "000":
        color_string = "=a"
    return color_string


def img_convert(image_array, art_char):
    (w, h, colors) = image_array.shape
    color_string = ''
    last_color = ''
    for x in range(0, w - 1):
        for y in range(0, h - 1):
            new_color = color_convert(image_array, x, y)
            if new_color != "=a":
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
    print('\\\\<ascii>' + color_string + '</ascii>')

    return color_string


inputdir = 'images'
outputdir = 'codes'
inputfile = 'dragonfly.png'
outputfile = ''
size = 40
character = '@'

try:
    image_name: str = inputdir + '/' + inputfile
    image_file = Image.open(image_name)
except:
    print(inputfile + ' is not found in the images directory.')
    sys.exit()
if outputfile == '':
    outputfile = inputfile.split(".")[0] + '.txt'
code_name: str = outputdir + '/' + outputfile
code_file = open(code_name, "w")

print('Input file is ' + image_name)
print('Output file is ' + code_name)
print('Converting for size: ' + str(size) + ', and character: ' + character)
image_sc = scale_down(image_file, size)
img_array = np.array(image_sc)
art_string = img_convert(img_array, character)
code_file.write(art_string)
code_file.close()
image_file.close()
