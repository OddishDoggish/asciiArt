import PIL
import numpy as np
import scipy as sp
from scipy.spatial import distance
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import filter

m = 8   # number of pixels of a letter (x)
w = 60  # number of characters across (x)
n = 16  # number of pixels of a letter (y)

white = 255
black = 0

foreground = white
background = black

fontname = "cour.ttf"

def scale_image(image, new_width, height_factor):
    """
    Resizes an image preserving the aspect ratio.
    """
    image = image.convert("L")
    (original_width, original_height) = image.size
    aspect_ratio = original_height/original_width
    new_height = height_factor * round(aspect_ratio * new_width / height_factor)
    new_image = image.resize((new_width, new_height))
    return new_image

#def convert_to_grayscale(image):
#    return image.convert('L')


def letterImage(letter, fontname, foreground, background, width, height):
    font = ImageFont.truetype(fontname, 10)
    img=Image.new("L", (width, height), background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), letter, foreground, font=font)
    draw = ImageDraw.Draw(img)
    return img


def letterArray(fontname, foreground, background, m, n):
    letter_array = np.array(letterImage(chr(32), fontname, foreground, background, m, n))
    letter_array = np.reshape(letter_array, letter_array.size)
    for letter in range(33, 126):
        letter_image = np.array(letterImage(chr(letter), fontname, foreground, background, m, n))
        letter_image = np.reshape(letter_image,letter_image.size)
        letter_array = np.concatenate((letter_array,letter_image))
    letter_array = np.reshape(letter_array,(126-32,m*n))
    return letter_array


def compare_partial(image, letter_image, m, n):
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
                dist = distance.mahalanobis(pic_vector, letter_vector, np.identity(m*n))
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
image = Image.open('cup.jpg')
image = image.convert("RGB")
#image = Image.open('sunflower.jpg')
print('Image opened.')


image = scale_image(image, m*w, n)
image = filter.edge(image)
image = filter.blur(image)

(width, height) = image.size
image_array = np.array(image)
for k in range(height):
    for j in range(width):
        if image_array[k, j] < 10:
            image_array[k, j] = 0
        else:
            image_array[k, j] = 255

image = Image.fromarray(image_array)
image.show()

letter_array = letterArray(fontname, foreground, background, m, n)

ascii_string = compare_partial(image, letter_array, m, n)

print(ascii_string)

