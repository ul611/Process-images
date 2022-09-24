from skimage.io import imread, imsave
import urllib.request

# Изменение цвета пикселя изображения
# Get image
link = urllib.request.url(
    'https://stepik.org/media/attachments/lesson/58180/tiger-color.png')
# Read image
img = imread(link)
# Get image shape
nrows, ncols, nchannels = img.shape
# Change central pixel
img[nrows // 2, ncols // 2] = [102, 204, 102]
# Save modified image
imsave('out_img.png', img)
