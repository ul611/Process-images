from skimage.io import imread
import urllib.request


# Количество столбцов
# Get image
link = urllib.request.urlopen("https://stepik.org/media/attachments/lesson/58180/img.png")
# Read image
img = imread(link)
# Print ncols
print(img.shape[1])
