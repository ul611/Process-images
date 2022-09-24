from skimage.io import imread, imsave
import numpy as np

from task_10_min_max_stable_5perc import min_max_brightness_for_stable_contrast
from task_9_autocontrast import linear_contrast_alignment


# read file
img = imread('img.png').astype('float')
# save transformed image
imsave('out_img.png',
       np.clip(linear_contrast_alignment(img, *min_max_brightness_for_stable_contrast(img)), 0, 255).astype('uint8'))


# fine solution
img = imread('img.png').astype(np.float32)
vmin, vmax = np.percentile(img, [5, 95])
img = 255 * (img - vmin) / (vmax - vmin)
img = np.clip(img, 0, 255).astype(np.uint8)
imsave('out_img.png', img)
