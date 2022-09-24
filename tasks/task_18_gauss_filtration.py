from tasks.task_17_gauss_kernel import gauss_kernel

from skimage.io import imread, imsave
import numpy as np
from scipy.signal import convolve2d


def gauss_filtration(img, sigma):
    kernel = gauss_kernel(sigma)
    return np.clip(convolve2d(img, kernel, mode='valid'), 0, 1) #.astype('uint8')


#img = imread('tiger-gray-small.png')
#sigma = 0.66
#img = gauss_filtration(img, sigma)


#imsave('out_img.png', img)
