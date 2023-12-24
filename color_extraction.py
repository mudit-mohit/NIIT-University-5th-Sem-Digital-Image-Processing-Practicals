import numpy as np
import cv2 as cv
# Read the image using OpenCV
img = cv.imread(r"C:\Dev\DIP\Open CV\photos\Lenna.png")
# Ensure the image is not None
if img is not None:
    # Split the image into channels using NumPy
    blue_channel, green_channel, red_channel = img[:, :, 0], img[:, :, 1], img[:, :, 2]
# Your custom logic here (for example, you can process the channels as needed)
# Display the channels using NumPy (you can replace this with your own logic)
    cv.imshow("Blue Channel", blue_channel)
    cv.imshow("Green Channel", green_channel)
    cv.imshow("Red Channel", red_channel)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Error: Image not loaded.")              
