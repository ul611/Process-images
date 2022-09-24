from skimage.io import imread, imsave
# import matplotlib.pyplot as plt
import numpy as np


def min_max_brightness(img):
    # matplotlib version
    # values, bin_edges, patches = plt.hist(init_img.ravel(), bins=range(257))
    # numpy version
    values, bin_edges = np.histogram(img, bins=range(257))
    bin_edges = bin_edges[:-1]
    min_brightness = bin_edges[values != 0][0]
    max_brightness = bin_edges[values != 0][-1]
    return min_brightness, max_brightness


# recalculate brightness for one pixel
def recalc_brightness(bright_px, min_brightness, max_brightness, scale=255):
    new_bright_px = (bright_px - min_brightness) * scale / (max_brightness - min_brightness)
    return round(new_bright_px, 2)


# linear alignment of contrast
def linear_contrast_alignment(img, min_brightness, max_brightness, scale=255):
    return np.vectorize(recalc_brightness)(img, min_brightness, max_brightness, scale)


# read file
img = imread('img.png')
# save transformed image
imsave('out_img.png',
       linear_contrast_alignment(img, *min_max_brightness(img)).astype('uint8'))


# гуманное решение
img = imread('img.png')
x_min, x_max = img.min(), img.max()
img_out = ((img - x_min) * (255 / (x_max - x_min))).astype('uint8')
imsave('out_img.png', img_out)
