import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
c = 255/np.log(1 + np.max(gray_img))
log_transform = c * np.log(1 + gray_img)
log_transform = np.array(log_transform, dtype=np.uint8)
cv.imshow("Original Image", img)
cv.imshow("Transformed Image", log_transform)
cv.waitKey(0)
cv.destroyAllWindows()
