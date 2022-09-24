from skimage.io import imread, imsave
import urllib.request


# Вычисление негатива изображения
# Get image
link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58181/tiger-color.png')
img = imread(link)
# Find negative of image
neg_img = 255 - img
# Save modified image
imsave('out_img.png', neg_img)
