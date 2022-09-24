from skimage.io import imread, imshow
from skimage.color import rgb2gray
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

# modify to gray with right brightness
r, g, b = np.dsplit(img_f, 3)
img_y = 0.2126 * np.squeeze(r, axis=2) + 0.7152 * np.squeeze(g, axis=2) + 0.0722 * np.squeeze(b, axis=2)
# or
img_y_skimage = rgb2gray(img_f)
