from skimage.io import imread, imsave
import numpy as np


def convolution_box_filtration(img, k=5):
    if k % 2 != 1:
        raise AttributeError('k must be odd')
    coef = 1 / k ** 2
    w, h = img.shape
    w, h = w - 2 * (k // 2), h - 2 * (k // 2)
    ret_img = np.zeros((w, h), dtype='int32')
    left = k
    while left:
        top = k
        left -= 1
        while top:
            top -= 1
            ret_img = ret_img + img[left:(left + w), top:(top + h)]

    return (ret_img * coef).astype('uint8')


img = imread('img.png')
img = convolution_box_filtration(img)
imsave('out_img.png', img)
