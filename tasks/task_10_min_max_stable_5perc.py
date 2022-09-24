from skimage.io import imread
import numpy as np


def min_max_brightness_for_stable_contrast(img, n_perc_to_drop=5) -> None:
    # number of pixels to drop (most dark and most light)
    k = round(img.size * n_perc_to_drop / 100)
    # histogram results for image
    values, bin_edges = np.histogram(img, bins=range(257))
    # cumulative sums for histogram values (from begin and from end)
    values_cumsum_begin = np.cumsum(values)
    values_cumsum_end = np.cumsum(values[::-1])[::-1]
    # find min and max brightness
    bin_edges = bin_edges[:-1]
    min_pix = bin_edges[values_cumsum_begin > k][0]
    max_pix = bin_edges[values_cumsum_end > k][-1]
    # print min and max brightness
    return min_pix, max_pix


# read image
img = imread('img.png')
# percent of pixels to drop (most dark and most light)
n_perc_to_drop = 5
# print minimum and maximum for stable  linear contrast correction
print(*min_max_brightness_for_stable_contrast(img, n_perc_to_drop))


# good solution
task_img = imread("img.png")
print(*np.percentile(task_img, q=(5, 95)).astype("uint8"))
