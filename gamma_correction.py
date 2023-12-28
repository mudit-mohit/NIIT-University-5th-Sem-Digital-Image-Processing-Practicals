import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gamma = 2.5
lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(256)]).astype(np.uint8)
img_corrected = cv.LUT(img, lookup_table)
cv.imshow("Original Image", img)
cv.imshow("Gamma Corrected Image", img_corrected)
cv.waitKey(0)
cv.destroyAllWindows()