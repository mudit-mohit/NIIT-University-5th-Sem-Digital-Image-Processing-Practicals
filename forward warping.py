import numpy as np
import cv2 as cv
img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png')
if img is not None:
    h, w, channels = img.shape
    out_img = np.zeros((h, w, channels), dtype=np.uint8)
    tx = 50  
    ty = 0   
    for y in range(h):
        for x in range(w):
            new_x = x + tx
            new_y = y + ty
            if 0 <= new_x < w and 0 <= new_y < h:
                out_img[new_y, new_x] = img[y, x]
    cv.imshow('Original Image', img)
    cv.imshow('Forward Warped Image', out_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image not found.")
