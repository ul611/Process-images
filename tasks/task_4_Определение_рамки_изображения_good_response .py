from skimage.io import imread
from skimage import img_as_float
import urllib.request
import numpy as np


# Определение рамки изображения
# Get image
link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58180/tiger-border.png')
img = imread(link)
# make a mask
a = np.where(img != img[0, 0])
# print answer
print("%i %i %i %i"%(a[1][0], a[0][0], img.shape[1] - 1 - a[1][-1], img.shape[0] - 1 - a[0][-1]))
