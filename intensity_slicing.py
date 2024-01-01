import numpy as np
import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
hsi_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue_channel = hsi_img[:, :, 0]
saturation_channel = hsi_img[:, :, 1]
intensity_channel = hsi_img[:, :, 2]
lower_intensity = 150
upper_intensity = 250
sliced_intensity = np.zeros_like(intensity_channel)
sliced_intensity[(intensity_channel >= lower_intensity) & (intensity_channel <= upper_intensity)] = 255
merged_hsi_img = cv.merge([hue_channel, saturation_channel, sliced_intensity])
merged_rgb_img = cv.cvtColor(merged_hsi_img, cv.COLOR_HSV2BGR)
cv.imshow("Original RGB Image", img)
cv.imshow("HSI Image", hsi_img)
cv.imshow("Merged Image", merged_rgb_img)
cv.waitKey(0)
cv.destroyAllWindows()