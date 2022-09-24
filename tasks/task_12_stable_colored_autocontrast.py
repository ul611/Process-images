from skimage.io import imread, imsave, imshow
from skimage.util import img_as_float, img_as_ubyte
import numpy as np

from tasks.task_9_autocontrast import linear_contrast_alignment


def RGB_to_YUV(img):
    R, G, B = np.dsplit(img, 3)
    del img
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    U = -0.0999 * R - 0.3360 * G + 0.4360 * B
    V = 0.6150 * R - 0.5586 * G - 0.0563 * B
    del R, G, B
    return Y, U, V


def min_max_brightness_for_stable_contrast2(img, k_to_drop=5) -> None:
    # find min and max brightness
    min_pix, max_pix = np.percentile(img.reshape(-1), (k_to_drop, 100 - k_to_drop))
    # print min and max brightness
    return min_pix, max_pix


def YUV_to_RGB(Y, U, V):
    R = Y + 1.2803 * V
    G = Y - 0.2148 * U - 0.3805 * V
    B = Y + 2.1279 * U
    del Y, U, V
    return np.dstack((R, G, B))


#img = imread('img.png')
#img = img_as_float(img)
#Y, U, V = RGB_to_YUV(img)
#Y = np.clip(linear_contrast_alignment(Y, *min_max_brightness_for_stable_contrast2(Y), scale=1), 0, 1)
#img = YUV_to_RGB(Y, U, V)
#img = np.clip(img, 0, 1)
#imsave('out_img.png', np.round((img * 255)).astype('uint8'))
