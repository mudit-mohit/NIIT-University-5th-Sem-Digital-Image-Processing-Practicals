import numpy as np
import cv2 as cv
# Read the image using OpenCV
img = cv.imread(r"C:\Dev\DIP\Open CV\photos\Lenna.png")
# Ensure the image is not None
if img is not None:
    # Convert the image to RGB color space using NumPy
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# Define the lower and upper bounds for the red color using NumPy
    lower_red = np.array([150, 0, 0], dtype=np.uint8)
    upper_red = np.array([255, 100, 100], dtype=np.uint8)
# Create a red mask using NumPy
    red_mask = np.all((img_rgb >= lower_red) & (img_rgb <= upper_red), axis=-1)
# Apply the mask to the original image using NumPy
    red_result = img_rgb.copy()
    red_result[~red_mask] = 0
# Display the original image, red mask, and result using OpenCV
    cv.imshow("Original Image", cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR))
    cv.imshow("Red Mask", red_mask.astype(np.uint8) * 255)
    cv.imshow("Red Result", cv.cvtColor(red_result, cv.COLOR_RGB2BGR))
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Error: Image not loaded.")