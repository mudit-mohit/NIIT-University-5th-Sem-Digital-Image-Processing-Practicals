import numpy as np
import cv2 as cv
from scipy.ndimage import gaussian_filter
from matplotlib import pyplot as plt
# Read the image using OpenCV
img = cv.imread('C:\Dev\DIP\Open CV\photos\IMG20200821113917.jpg')
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Define a kernel for Gaussian blur
sigma = 1.0
# Apply Gaussian blur to the grayscale image using scipy
blur = gaussian_filter(gray, sigma=sigma)
# Calculate the unsharp mask using NumPy
unsharp_mask = gray - blur
# High-boost filtering parameters
boost_factor = 2.0
# Calculate the high-boost filtered image using NumPy
high_boost = gray + boost_factor * unsharp_mask
# Clip pixel values to be in the valid range [0, 255] using NumPy
high_boost = np.clip(high_boost, 0, 255)
# Convert back to 3-channel (BGR) if needed using NumPy
high_boost_colored = cv.cvtColor(high_boost.astype(np.uint8), cv.COLOR_GRAY2BGR)
# Display the original and processed images using OpenCV
cv.imshow('Original Image', img)
cv.imshow('High-Boost Filtered Image', high_boost_colored)
cv.waitKey(0)
cv.destroyAllWindows()
# Display the unsharp mask using Matplotlib
plt.imshow(unsharp_mask, cmap='gray')
plt.title('Unsharp Mask')
plt.show()
