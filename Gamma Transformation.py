import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
gamma = 1.5
gamma_corrected = np.power(img / 255.0, gamma)
gamma_corrected = (gamma_corrected * 255).astype(np.uint8)
cv.imshow("Original Image", img)
cv.imshow("Gamma Corrected Image", gamma_corrected)
cv.waitKey(0)
cv.destroyAllWindows()
