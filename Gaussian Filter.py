import numpy as np
import cv2 as cv
image_path = "C:\Dev\DIP\Open CV\photos\Lenna.png"
img = cv.imread(image_path)
if img is None:
    print("Image not found or could not be loaded.")
else:
    kernel_size = 9
    sigma = 1.0
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * 
                      np.exp(-((x - (kernel_size - 1) / 2) ** 2 + 
                               (y - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (kernel_size, kernel_size)
    )
    kernel /= np.sum(kernel)
    blurred_image = cv.filter2D(img, -1, kernel)
    cv.imshow("Original Image", img)
    cv.imshow("Blurred Image", blurred_image)
    output_path = 'custom_blurred_image.png'
    cv.imwrite(output_path, blurred_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
