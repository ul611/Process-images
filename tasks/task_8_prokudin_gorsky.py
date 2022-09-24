from skimage.io import imread, imsave
from skimage.morphology import disk
from skimage import img_as_float, img_as_ubyte
from skimage.filters import threshold_otsu, threshold_isodata, threshold_li, threshold_mean, threshold_triangle, threshold_yen, rank, threshold_niblack, threshold_sauvola
import numpy as np
# import urllib.request as urt
# from task_4_find_image_borders import find_borders_width



# Сопоставление фотографий Прокудина-Горского
# Get image
img = imread('01.png')
# binarize image with Otsu thresholding method to easier find the borders
# thresh = threshold_otsu(img)
# binary = img > thresh
# # find white borders
# mask = np.where(img != img[0, 0])
# left, up, right, down = mask[1][0], mask[0][0], img.shape[1] - 1 - mask[1][-1], \
#                         img.shape[0] - 1 - mask[0][-1]


img_f = img_as_float(img)


def align(img_f, g_coord):
    row_g, col_g = g_coord
    # Crop white borders
    # binarize image with Otsu thresholding method to easier find the borders
    thresh = threshold_otsu(img)
    binary = img > thresh
    # find white borders
    mask = np.where(binary != binary[0, 0])
    left_c, up_c, right_c, down_c = mask[1][0], mask[0][0], mask[1][-1], mask[0][-1]
    # crop white borders
    img_f = img_f[up_c:down_c, left_c:right_c]
    # split channels
    third = img_f.shape[0] // 3
    b = img_f[:third, :]
    g = img_f[third:(2 * third), :]
    r = img_f[(2 * third):(3 * third), :]
    # Crop black borders
    # calc % of image that would be enough to crop
    pers15 = img_f.shape[1] * 15 // 100
    b = b[pers15:-pers15, pers15:-pers15]
    g = g[pers15:-pers15, pers15:-pers15]
    r = r[pers15:-pers15, pers15:-pers15]
    # calc shifts
    roll = 15
    # first, let's convert images into bw format

    # window_size = 25
    # thresh_b = threshold_niblack(b, window_size=window_size, k=1.9)
    # b_bw = b > thresh_b
    # thresh_g = threshold_niblack(g, window_size=window_size, k=1.9)
    # g_bw = g > thresh_g
    # thresh_r = threshold_niblack(r, window_size=window_size, k=1.9)
    # r_bw = r > thresh_r

    # window_size = 25
    # thresh_b = threshold_sauvola(b, window_size=window_size)
    # b_bw = b > thresh_b
    # thresh_g = threshold_sauvola(g, window_size=window_size)
    # g_bw = g > thresh_g
    # thresh_r = threshold_sauvola(r, window_size=window_size)
    # r_bw = r > thresh_r

    # thresh_b = threshold_yen(b)
    # b_bw = b > thresh_b
    # thresh_g = threshold_yen(g)
    # g_bw = g > thresh_g
    # thresh_r = threshold_yen(r)
    # r_bw = r > thresh_r

    # thresh_b = threshold_triangle(b)
    # b_bw = b > thresh_b
    # thresh_g = threshold_triangle(g)
    # g_bw = g > thresh_g
    # thresh_r = threshold_triangle(r)
    # r_bw = r > thresh_r

    # thresh_b = threshold_mean(b)
    # b_bw = b > thresh_b
    # thresh_g = threshold_mean(g)
    # g_bw = g > thresh_g
    # thresh_r = threshold_mean(r)
    # r_bw = r > thresh_r

    thresh_b = threshold_li(b)
    b_bw = b > thresh_b
    thresh_g = threshold_li(g)
    g_bw = g > thresh_g
    thresh_r = threshold_li(r)
    r_bw = r > thresh_r

    # thresh_b = threshold_isodata(b)
    # b_bw = b > thresh_b
    # thresh_g = threshold_isodata(g)
    # g_bw = g > thresh_g
    # thresh_r = threshold_isodata(r)
    # r_bw = r > thresh_r

    # radius = 4
    # footprint = disk(radius)
    # local_otsu_b = rank.otsu(b, footprint)
    # b_bw = b >= local_otsu_b
    # local_otsu_g = rank.otsu(g, footprint)
    # g_bw = g >= local_otsu_g
    # local_otsu_r = rank.otsu(r, footprint)
    # r_bw = r >= local_otsu_r

    # thresh_b = threshold_otsu(b)
    # b_bw = b > thresh_b
    # thresh_g = threshold_otsu(g)
    # g_bw = g > thresh_g
    # thresh_r = threshold_otsu(r)
    # r_bw = r > thresh_r

    # calc correlations between red channel and green channel
    corr_matrix = np.zeros((roll * 2 + 1, roll * 2 + 1), dtype=int)
    for i in np.arange(-roll, roll + 1):
        for j in np.arange(-roll, roll + 1):
            corr_matrix[i + roll, j + roll] = (np.roll(np.roll(r_bw, i, axis=0), j, axis=1) * g_bw).sum()
    row_r, col_r = np.unravel_index(np.argmax(corr_matrix), corr_matrix.shape)
    row_r, col_r = row_r - roll, col_r - roll
    # calc correlations between blue channel and green channel
    corr_matrix = np.zeros((roll * 2 + 1, roll * 2 + 1), dtype=int)
    for i in np.arange(-roll, roll + 1):
        for j in np.arange(-roll, roll + 1):
            corr_matrix[i + roll, j + roll] = (
                        np.roll(np.roll(b_bw, i, axis=0), j, axis=1) * g_bw).sum()
    row_b, col_b = np.unravel_index(np.argmax(corr_matrix), corr_matrix.shape)
    row_b, col_b = row_b - roll, col_b - roll
    # move green pixel
    row_r = row_g - row_r + third
    col_r = col_g - col_r
    row_b = row_g - row_b - third
    col_b = col_g - col_b
    return (row_b, col_b), (row_r, col_r)


print(align(img_f, (483, 218)))

# image    (row_g, col_g)    (row_b,col_b,row_r,col_r)
# # 00.png    (508, 237)        ((153, 237), (858, 238))
# # 01.png    (483, 218)        ((145, 219), (817, 218))
# # 02.png    (557, 141)        ((204, 143), (908, 140))
# # 03.png    (627, 179)        ((243, 179), (1010, 176))
# # 04.png    (540, 96)         ((154, 95), (922, 94))
# # 05.png    (641, 369)        ((258, 372), (1021, 368))
# # 06.png    (527, 196)        ((144, 198), (908, 193))
# # 07.png    (430, 140)        ((82, 140), (777, 141))
# # 08.png    (502, 254)        ((123, 259), (880, 251))
# # 09.png    (493, 238)        ((114, 240), (871, 235))
