from skimage.io import imread, imsave
import numpy as np


def convolution(img, kernel):
    if kernel.size % 2 != 1:
        raise AttributeError('kernel size must be odd')
    k = kernel.shape[0]
    w, h = img.shape
    w, h = w - 2 * (k // 2), h - 2 * (k // 2)
    ret_img = np.zeros((w, h), dtype=float)
    for i in range(w):
        for j in range(h):
            ret_img[i, j] = (kernel * img[i:(i + k), j:(j + k)]).sum()

    return ret_img


def sharpening(img, kernel=0.1*np.array([[-1, -2, -1],
                                         [-2, 22, -2],
                                         [-1, -2, -1]])
               ):
    return np.clip(convolution(img, kernel), 0, 255).astype('uint8')


img = imread('img.png')
img = sharpening(img)
imsave('out_img.png', img)
