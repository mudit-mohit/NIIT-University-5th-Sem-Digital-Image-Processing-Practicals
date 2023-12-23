import numpy as np
import cv2 as cv
# Read the image using OpenCV
img = cv.imread(r"C:\Dev\DIP\Open CV\photos\Lenna.png")
# Ensure the image is not None
if img is not None:
    # Convert the image to RGB color space
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# Convert the RGB image to HSI color space
    img_hsi = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV)
# Split the HSI channels
    h, s, i = cv.split(img_hsi)
# Perform color complement operation
    complement_i = 255 - i
    complement_s = 255 - s
# Merge the channels back to HSI
    complement_hsi = cv.merge([h, complement_s, complement_i])
# Convert back to RGB color space
    complement_rgb = cv.cvtColor(complement_hsi, cv.COLOR_HSV2RGB)
# Display the original and color complemented images
    cv.imshow("Original Image", cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR))
    cv.imshow("Color Complemented Image", complement_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Error: Image not loaded.")
