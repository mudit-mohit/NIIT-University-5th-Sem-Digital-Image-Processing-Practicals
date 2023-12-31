import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
def hist_equal(image):
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    equal_img = cdf[image]
    return equal_img
img_path = 'C:\Dev\DIP\Open CV\photos\Lenna.png'  
img = cv.imread(img_path, 0)  
enhance_img = hist_equal(img)
cv.imshow('Original Image', img)
cv.imshow('Enhanced Image', enhance_img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(img.flatten(), 256, [0, 256], color='b')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Frequency')
plt.subplot(1, 2, 2)
plt.hist(enhance_img.flatten(), 256, [0, 256], color='r')
plt.title('Enhanced Image Histogram')
plt.xlabel('Pixel Values')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
