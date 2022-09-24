from skimage.io import imread, imshow, imsave
from matplotlib import pyplot as plt


# Read image
img = imread('tiger-color.png')
# Crop the nose area
nose = img[370:410, 350:440]
imshow(nose)
plt.show()
# Change nose area color
img[370:410, 350:440] = [255, 0, 255]  # magenta
imshow(img)
plt.show()


# Copying images
img_yellow = imread('tiger-color-yellow-nose.png')
imshow(img_yellow[370:410, 350:440])
plt.show()
img_assigned = img_yellow  # incorrect way
img_copy = img_yellow.copy()  # right way
# Change nose color in the initial image
img_yellow[370:410, 350:440] = [255, 0, 255]
# with incorrect way
imshow(img_assigned)
plt.show()
# with right way
imshow(img_copy)
plt.show()
