import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png", cv.IMREAD_GRAYSCALE)
threshold_value = 128
thresholded_image = np.zeros_like(img)
thresholded_image[img >= threshold_value] = 255
cv.imshow("Original Image", img)
cv.imshow("Thresholded Image", thresholded_image)
cv.waitKey(0)
cv.destroyAllWindows()
