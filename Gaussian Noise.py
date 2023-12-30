import cv2
import numpy as np
import random
# Load the original image
original_img = cv2.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
mean = 0
stddev = 180
height, width, channels = original_img.shape
noise = np.zeros((height, width, channels), dtype=np.uint8)
# Generate Gaussian noise for each channel separately
for channel in range(channels):
    for y in range(height):
        for x in range(width):
            noise[y, x, channel] = np.uint8(random.gauss(mean, stddev))
# Add noise to the original image
noisy_img = cv2.add(original_img, noise)
output_img = np.concatenate((original_img, noisy_img), axis=1)
cv2.imshow('Original vs Noisy Image', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the noisy image
cv2.imwrite('C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg', noisy_img)