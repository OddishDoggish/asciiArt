import numpy as np
import scipy as sp
from scipy import signal
from PIL import Image


def kuwahara(image):
    pad = 2

    X = np.array(image)

    (m, n, c) = X.shape

    Xpad = np.zeros((m+2*pad+1, n+2*pad+1))
    Xpad[pad:m+pad, pad:n+pad] = X[:, :, 1]
    Y = X

    for j in range(pad, m+pad):
        for k in range(pad, n+pad):
            nw = Xpad[j - pad:j + 1, k - pad:k + 1]
            sw = Xpad[j:j + pad + 1, k - pad:k + 1]
            se = Xpad[j:j + pad + 1, k:k + pad + 1]
            ne = Xpad[j - pad:j + 1, k:k + pad + 1]


            s = np.array((np.var(nw), np.var(ne), np.var(sw), np.var(se)))
            m = np.array((np.mean(nw), np.mean(ne), np.mean(sw), np.mean(se)))

            Y[j-pad, k-pad, 1] = m[np.argmin(s)]

    return Y


def edge(image):
    image_array = np.array(image)
    kernel_edge = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    sfedge = signal.convolve2d(image_array, kernel_edge, mode='same')
    picture = Image.fromarray(sfedge)
    return picture


def blur(image):
    image_array = np.array(image)
    kernel_blur = np.array([[1/256, 4/256, 6/256, 4/256, 1/256], [4/256, 16/256, 24/256, 16/256, 4/256], [6/256,
        24/256, 36/256, 24/256, 6/256], [4/256, 16/256, 24/256, 16/256, 4/256], [1/256, 4/256, 6/256, 4/256, 1/256]])
    sfblur = signal.convolve2d(image_array, kernel_blur, mode='same')
    picture = Image.fromarray(sfblur)
    return picture



"""
image = Image.open('sunflower.jpg')
kimage = kuwahara(image)
picture = Image.fromarray(kimage)
picture.show()


image_array = np.array(image)

kernel_edge = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
kernel_edge = np.array([[1, 2, 0, -2, -1], [4, 8, 0, -8, -4], [6, 12, 0, -12, 6], [4, 8, 0, -8, -4], [1, 2, 0, -2, -1]])

sfedge = signal.convolve2d(image_array[:, :, 1], kernel_edge, mode='same')

picture = Image.fromarray(sfedge)
picture.show()
"""