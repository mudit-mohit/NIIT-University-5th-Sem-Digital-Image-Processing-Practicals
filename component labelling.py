import numpy as np
import cv2 as cv
from scipy import ndimage
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png', 0)
thresh_value = 127  
binary_img = np.where(img > thresh_value, 1, 0).astype(np.uint8)
def connected_components(binary_img):
    labeled_img, num_features = ndimage.label(binary_img)
    return labeled_img, num_features
labeled_components, num_labels = connected_components(binary_img)
colors = np.random.randint(0, 255, size=(num_labels + 1, 3))
labeled_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
for label in range(1, num_labels + 1):
    labeled_img[labeled_components == label] = colors[label]
cv.imshow('Original Image', img)
cv.imshow('Labeled Components', labeled_img)
cv.waitKey(0)
cv.destroyAllWindows()

