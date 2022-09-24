from skimage.io import imread, imsave
import numpy as np


def histogram_alignment(img):
    # histogram
    values, _ = np.histogram(img, bins=range(257))
    cdf = np.cumsum(values)
    cdf_min = cdf[cdf != 0][0]
    aligned_hist = np.round((cdf - cdf_min) * 255 / img.size)
    img = aligned_hist[img]
    return img


img = imread('img.png')
img = histogram_alignment(img).astype('uint8')
imsave('out_img.png', img)
