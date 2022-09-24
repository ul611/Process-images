from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt


# Read image
img = imread('tiger-color.png')
# Show image
imshow(img)
plt.show()
# Print image shape (nrows, ncols, nchannels)
print(img.shape)
# Take one pixel to get rgb channels information
print(img[383, 374])
# Rewrite color of pixel
img[383, 374] = [255, 255, 0]  # yellow
# Save modified image
imsave('tiger-color-yellow-nose.png', img)

