import numpy as np
import cv2 as cv
def intensity_level_slicing(img, low, up):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    slice_img = np.copy(gray_img)
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            pixel_value = gray_img[i, j]
            if low <= pixel_value <= up:
                slice_img[i, j] = 255  
    return slice_img
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png')
if img is not None:
    low_bound = 100
    up_bound = 200
    res_img = intensity_level_slicing(img, low_bound, up_bound)
    cv.imshow('Original Image', img)
    cv.imshow('Sliced Image', res_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image not found.")
