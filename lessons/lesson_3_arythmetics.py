from skimage.io import imread, imshow
from skimage import img_as_float
import matplotlib.pyplot as plt
import numpy as np


# Read image
img = imread('tiger-color.png')
# Show image
imshow(img)
plt.show()

print(img.max(), img.min())
# cast img to float
img_f = img_as_float(img)
print(img_f.max(), img_f.min())

# Reduce brightness (or contrast)
# colors became closer
imshow(img_f / 1.5)
plt.show()

imshow(img_f / 2)
plt.show()

imshow(img_f / 4)
plt.show()

# Reduce contract and add light (whiteness)
imshow(img_f / 4 + 0.25)
plt.show()

# Increase contrast with multiplying (care about float image limits)
# colors became farer
imshow(np.clip(img_f * 1.5, 0, 1))
plt.show()

imshow(np.clip(img_f * 2, 0, 1))
plt.show()

# Contrast and dark image
imshow(np.clip(img_f * 2 - 0.5, 0, 1))
plt.show()
