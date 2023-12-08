import numpy as np
import cv2 as cv
def custom_erose(img, kernel):
    res = np.zeros_like(img)
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    for y in range(pad_h, img.shape[0] - pad_h):
        for x in range(pad_w, img.shape[1] - pad_w):
            region = img[y - pad_h:y + pad_h + 1, x - pad_w:x + pad_w + 1]
            res[y, x] = np.min(region * kernel)
    return res
def custom_dilate(img, kernel):
    res = np.zeros_like(img)
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    for y in range(pad_h, img.shape[0] - pad_h):
        for x in range(pad_w, img.shape[1] - pad_w):
            region = img[y - pad_h:y + pad_h + 1, x - pad_w:x + pad_w + 1]
            res[y, x] = np.max(region * kernel)
    return res
def main():
    img = cv.imread('C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg', cv.IMREAD_GRAYSCALE)
    kernel = np.ones((5, 5), np.uint8)
    erose_res = custom_erose(img, kernel)
    open_res = custom_dilate(erose_res, kernel)
    cv.imshow('Original Image', img)
    cv.imshow('Opening Result', open_res)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()
