from skimage.io import imread, imsave
from skimage.util import img_as_float, img_as_ubyte
import numpy as np


def gray_world_transformation(img):
    # divide channels
    r, g, b = np.dsplit(img, 3)
    # find mean values by channel and for the entire image
    r_avg, g_avg, b_avg = np.mean(img, axis=(0, 1))
    img_avg = np.mean(img)
    # calc 'gray world' transformation coefficients
    r_w, g_w, b_w = r_avg / img_avg, g_avg / img_avg, b_avg / img_avg
    # recalc channels
    r, g, b = r / r_w, g / g_w, b / b_w
    img = np.dstack((r, g, b))
    return np.clip(img, 0, 1)


img = img_as_float(imread('img.png'))
img = gray_world_transformation(img)
imsave('out_img.png', img_as_ubyte(img))


# good solution
def gray_world(img):
    rgb_means = img.mean(axis=(0, 1))
    return img_as_ubyte(np.clip(img * rgb_means.mean() / rgb_means, 0, 1))