import numpy as np
import cv2 as cv
input_img = cv.imread('C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg', cv.IMREAD_GRAYSCALE)
input_img_colored = cv.cvtColor(input_img, cv.COLOR_GRAY2BGR)
output_img = np.zeros_like(input_img_colored)
output_img[(input_img >= 0) & (input_img < 50), 0] = input_img[(input_img >= 0) & (input_img < 50)] + 50
output_img[(input_img >= 0) & (input_img < 50), 1] = input_img[(input_img >= 0) & (input_img < 50)] + 100
output_img[(input_img >= 0) & (input_img < 50), 2] = input_img[(input_img >= 0) & (input_img < 50)] + 10
output_img[(input_img >= 50) & (input_img < 100), 0] = input_img[(input_img >= 50) & (input_img < 100)] + 35
output_img[(input_img >= 50) & (input_img < 100), 1] = input_img[(input_img >= 50) & (input_img < 100)] + 128
output_img[(input_img >= 50) & (input_img < 100), 2] = input_img[(input_img >= 50) & (input_img < 100)] + 10
output_img[(input_img >= 100) & (input_img < 150), 0] = input_img[(input_img >= 100) & (input_img < 150)] + 152
output_img[(input_img >= 100) & (input_img < 150), 1] = input_img[(input_img >= 100) & (input_img < 150)] + 130
output_img[(input_img >= 100) & (input_img < 150), 2] = input_img[(input_img >= 100) & (input_img < 150)] + 15
output_img[(input_img >= 150) & (input_img < 200), 0] = input_img[(input_img >= 150) & (input_img < 200)] + 50
output_img[(input_img >= 150) & (input_img < 200), 1] = input_img[(input_img >= 150) & (input_img < 200)] + 140
output_img[(input_img >= 150) & (input_img < 200), 2] = input_img[(input_img >= 150) & (input_img < 200)] + 25
output_img[(input_img >= 200) & (input_img <= 256), 0] = input_img[(input_img >= 200) & (input_img <= 256)] + 120
output_img[(input_img >= 200) & (input_img <= 256), 1] = input_img[(input_img >= 200) & (input_img <= 256)] + 160
output_img[(input_img >= 200) & (input_img <= 256), 2] = input_img[(input_img >= 200) & (input_img <= 256)] + 45
cv.imshow('Input Image', input_img_colored)
cv.imshow('Pseudo Colored Image', output_img)
cv.waitKey(0)
cv.destroyAllWindows()