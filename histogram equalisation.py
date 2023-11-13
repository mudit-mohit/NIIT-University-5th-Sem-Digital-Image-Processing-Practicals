import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png', 0)  
hist, _ = np.histogram(img.flatten(), bins=256, range=(0, 256))
cdf = hist.cumsum()
cdf_normal = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
equal_img = np.interp(img.flatten(), range(0, 256), cdf_normal).reshape(img.shape)
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equal_img, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()





