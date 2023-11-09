import numpy as np
import cv2 as cv
input_img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png')
r, c = input_img.shape[:2]
output_img = np.zeros_like(input_img)
for i in range(r):
    for j in range(c):
        new_i = r - i - 1  
        new_j = c - j - 1
        if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
            output_img[new_i, new_j] = input_img[i, j]
cv.imshow('Input Image', input_img)
cv.imshow('Output Image - Backward Warping', output_img)
cv.waitKey(0)
cv.destroyAllWindows()
