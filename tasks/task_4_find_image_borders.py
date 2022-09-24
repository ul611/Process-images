from skimage.io import imread
import urllib.request
import numpy as np


# Определение рамки изображения
# Get image
# link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58180/tiger-border.png')
# img = imread(link)

def find_borders_width(img):

    # Define target color
    target_color = img[0, 0]

    # one corner
    border_up = 1
    border_left = 1
    pixel = img[border_up - 1, border_left - 1]
    # go on diagonal
    while np.array_equal(pixel, target_color):
        border_up += 1
        border_left += 1
        pixel = img[border_up - 1, border_left - 1]
    # find back upper border
    while not np.array_equal(pixel, target_color):
        border_up -= 1
        pixel = img[border_up - 1, border_left - 1]
    # find back left border
    pixel = img[border_left - 1, border_left - 1]
    while not np.array_equal(pixel, target_color):
        border_left -= 1
        pixel = img[border_up, border_left - 1]

    # second corner
    h, w = img.shape[0:2]
    border_down = 1
    border_right = 1
    pixel = img[h - border_down, w - border_right]
    # go on diagonal
    while np.array_equal(pixel, target_color):
        border_down += 1
        border_right += 1
        pixel = img[h - border_down, w - border_right]
    # find back bottom border
    while not np.array_equal(pixel, target_color):
        border_down -= 1
        pixel = img[h - border_down, w - border_right]
    # find back right border
    pixel = img[h - border_right, w - border_right]
    while not np.array_equal(pixel, target_color):
        border_right -= 1
        pixel = img[h - border_down - 1, w - border_right]
    # answer
    return border_left, border_up, border_right, border_down


