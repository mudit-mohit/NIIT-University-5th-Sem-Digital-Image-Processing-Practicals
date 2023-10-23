import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png", cv.IMREAD_GRAYSCALE)  
min_pixel = np.min(img)
max_pixel = np.max(img)
new_min = 0
new_max = 255
stretched_img = ((img - min_pixel)/(max_pixel - min_pixel)) * (new_max - new_min) +  new_min
stretched_img = stretched_img.astype(np.uint8)
cv.imshow("Original Image", img)
cv.imshow("Stretched Image", stretched_img)
cv.waitKey(0)
cv.destroyAllWindows()
