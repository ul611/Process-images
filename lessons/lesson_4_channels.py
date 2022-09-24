from skimage.io import imread, imshow
from skimage import img_as_float
import matplotlib.pyplot as plt
import numpy as np


# Read image
img = imread('tiger-color.png')
# Show image
imshow(img)
plt.show()

# cast img to float
img_f = img_as_float(img)

# extract channels
r = img_f[:, :, 0]  # red channel
imshow(r)
plt.show()
g = img_f[:, :, 1]  # green channel
imshow(g)
plt.show()
b = img_f[:, :, 2]  # blue channel
imshow(b)
plt.show()

# combine colored image from channels
img_combined = np.dstack((r, g, b))
imshow(img_combined)
plt.show()
# a little bit of experiments
img_combined2 = np.dstack((g, r, b))
imshow(img_combined2)
plt.show()
img_combined3 = np.dstack((r, b, g))
imshow(img_combined3)
plt.show()

# average image from 3 channels
avg_gray = (r + g + b) / 3
imshow(avg_gray)
plt.show()
