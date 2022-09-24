from skimage.io import imread, imsave
import numpy as np


def median_blur(img, kernel=(7, 7)):
    k_w, k_h = kernel
    if k_w * k_h % 2 != 1:
        raise AttributeError('kernel size must be odd')
    w, h = img.shape
    w, h = w - 2 * (k_w // 2), h - 2 * (k_h // 2)
    ret_img = np.zeros((w, h), dtype='uint8')
    for i in range(w):
        for j in range(h):
            ret_img[i, j] = np.median(img[i:(i + k_w), j:(j + k_h)])
    return ret_img


img = imread('tiger-gray-small.png')
img = median_blur(img)
imsave('out_img.png', img)
