import PIL
import numpy as np
import scipy as sp
from scipy.spatial import distance
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import filter

m = 8   # number of pixels of a letter (x)
w = 80  # number of characters across (x)
n = 16  # number of pixels of a letter (y)
channels = 1 # 3 for RGB, 1 for grayscale
white = (255,255,255)
black = (0,0,0)

foreground = white
background = black

fontname = "cour.ttf"

def scale_image(image, new_width, height_factor, channels):
    """Resizes an image preserving the aspect ratio.
    """
    if channels == 3:
        image = image.convert("RGB")
    else:
        image = image.convert("L")
    (original_width, original_height) = image.size
    aspect_ratio = original_height/original_width
    new_height = height_factor * round(aspect_ratio * new_width / height_factor)
    new_image = image.resize((new_width, new_height))
    return new_image

#def convert_to_grayscale(image):
#    return image.convert('L')


def letterImage(letter, fontname, foreground, background, width, height, channels):
    font = ImageFont.truetype(fontname, 10)
    img=Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), letter, foreground, font=font)
    draw = ImageDraw.Draw(img)
    if channels != 3:
        img = img.convert("L")
#    img.save(letter + "_test.png")
    return img


def letterArray(fontname, foreground, background, m, n, channels):
    letter_array = np.array(letterImage(chr(32), fontname, foreground, background, m, n, channels))
    letter_array = np.reshape(letter_array, letter_array.size)
    for letter in range(33, 126):
        letter_image = np.array(letterImage(chr(letter), fontname, foreground, background, m, n, channels))
        letter_image = np.reshape(letter_image,letter_image.size)
        letter_array = np.concatenate((letter_array,letter_image))
    letter_array = np.reshape(letter_array,(126-32,m*n*channels))
    return letter_array


def compare_partial(image, letter_image, m, n, channels):
    picture = np.array(image)
    chosen_str = ''
    (width, height) = image.size
    for k in range(0, height-n-1, n):
        for j in range(0, width-m-1, m):
            print(str(k) + ", " + str(j))
            choice = 10000
            for letter in range(0,94):
                pic_vector = np.reshape(picture[k:k+n,j:j+m],picture[k:k+n,j:j+m].size)
                letter_vector = letter_image[letter,:]
                dist = distance.mahalanobis(pic_vector, letter_vector, np.identity(m*n*channels))
                if choice > dist:
                    choice = dist
                    if letter == 91 or letter == 92:
                        chosen = '|' + chr(letter+32)
                    else:
                        chosen = chr(letter+32)
            chosen_str = chosen_str + chosen
        chosen_str = chosen_str + '|/'
    return chosen_str


#image = Image.open('Osmium3.jpg')
#image = Image.open('dolphinBW.png')
image = Image.open('sunflower.jpg')
print('Image opened.')

image = filter.edge(image)

image_sc = scale_image(image, m*w, n, channels)
image_sc.show()

letter_array = letterArray(fontname, foreground, background, m, n, channels)

ascii_string = compare_partial(image_sc, letter_array, m, n, channels)

print(ascii_string)

