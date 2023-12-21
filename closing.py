import numpy as np
import cv2 as cv
def custom_close(img, kernel):
    dilated = cv.dilate(img, kernel, iterations=1)
    closed = cv.erode(dilated, kernel, iterations=1)
    return closed
def main():
    img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png', cv.IMREAD_GRAYSCALE)
    kernel = np.ones((5, 5), np.uint8)
    custom_close_res = custom_close(img, kernel)
    cv.imshow('Original Image', img)
    cv.imshow('Custom Closing Result', custom_close_res)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()
