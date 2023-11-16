import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png', cv.IMREAD_GRAYSCALE)  
MAX_PIX_VAL = 256
histogram = np.zeros(MAX_PIX_VAL, dtype=int)
r, c = img.shape
for i in range(r):
    for j in range(c):
        pix_val = img[i, j]
        histogram[pix_val] += 1
plt.figure(figsize=(8, 6))
plt.bar(np.arange(MAX_PIX_VAL), histogram, color='gray')
plt.title('Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
