from skimage.io import imread, imsave
import numpy as np
import urllib.request


# Вычисление негатива изображения
# Get image
link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58181/tiger-color.png')
img = imread(link)
# split channels
r, g, b = np.dsplit(img, 3)
# revert channels
img_brg = np.dstack((b, r, g))
# Save modified image
imsave('out_img.png', img_brg)

# other way to do this

# img = imread('img.png')
# img[:, :, [0, 1, 2]] = img[:, :, [2, 0, 1]]
# imsave('out_img.png', img)
