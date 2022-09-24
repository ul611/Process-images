from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np
import urllib.request


# Вычисление негатива изображения
# Get image
# link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58181/tiger-color.png')
# img = imread(link)
img = imread('tiger-color.png')
# convert image to float
img_f = img_as_float(img)
# split channels
r, g, b = np.dsplit(img_f, 3)
# calc brightness
img_y = 0.2126 * np.squeeze(r, axis=2) + 0.7152 * np.squeeze(g, axis=2) + 0.0722 * np.squeeze(b, axis=2)
# convert image to bytes
img_out = img_as_ubyte(img_y)
# Save modified image
imsave('out_img.png', img_out)

# another way
imsave('out_img.png', img_as_ubyte(np.dot(img_as_float(imread('tiger-color.png')), [0.2126, 0.7152, 0.0722])))
