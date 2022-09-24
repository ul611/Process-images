from skimage.io import imread, imsave
import urllib.request


# Изменение цвета прямоугольника
# Get image
link = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/58180/tiger-gray.png')
img = imread(link)
# Find central pixel
nrows, ncols, _ = img.shape
crow, ccol = nrows // 2, ncols // 2
# Change rectangle area color
img[crow-3:crow+4, ccol-7:ccol+8] = [255, 192, 203]
# Save modified image
imsave('out_img.png', img)
