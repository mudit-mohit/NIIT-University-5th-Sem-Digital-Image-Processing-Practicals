import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png', 0)  
window_size = 128  
h, w = img.shape
equal_img = np.zeros_like(img)
for y in range(0, h - window_size, window_size):
    for x in range(0, w - window_size, window_size):
        window = img[y:y+window_size, x:x+window_size]
        hist, _ = np.histogram(window.flatten(), bins=256, range=(0, 256))
        cdf = hist.cumsum()
        cdf_normal = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
        equal_window = np.interp(window.flatten(), range(0, 256), cdf_normal).reshape(window.shape)
        equal_img[y:y+window_size, x:x+window_size] = equal_window
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Local Histogram Equalized Image')
plt.imshow(equal_img, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
