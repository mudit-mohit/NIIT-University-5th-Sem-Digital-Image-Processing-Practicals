import numpy as np
import cv2 as cv
def eros(img, k):
    res = np.zeros_like(img)
    h, w = k.shape
    padding = h//2, w//2
    for y in range(padding[0], img.shape[0] - padding[0]):
        for x in range(padding[1], img.shape[1] - padding[1]):
            reg = img[y - padding[0]: y + padding[0] + 1, x - padding[1]: x + padding[1] + 1]
            res[y ,x] = np.min(reg * k)
    return res
def dilat(img, k):
    res = np.zeros_like(img)
    h , w = k.shape
    padding = h//2, w//2
    for y in range(padding[0], img.shape[0] - padding[0]):
        for x in range(padding[1], img.shape[1] - padding[1]):
            reg = img[y - padding[0]: y + padding[0] + 1, x - padding[1]: x + padding[1] + 1]
            res[y, x] = np.max(reg * k)
    return res
def hole_fill(img, k, start_x, start_y):
    i = 5
    res = img.copy()
    padding = k.shape[0] // 2
    start_x = max(padding, min(start_x, img.shape[0] - 1 - padding))
    start_y = max(padding, min(start_y, img.shape[1] - 1 - padding))
    for _ in range(i):
        dilat_img = dilat(res, k)
        res = np.minimum(dilat_img, 255 - img)
    return res
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png", 0)
thresh_val = 128
bin_img = np.where(img >= thresh_val, 255, 0).astype(np.uint8)
k = np.ones((3,3), dtype=np.uint8)
eros_img = eros(img, k)
bound_img = img - eros_img
#open_img = dilat(eros_img, k)
dilat_img = dilat(img, k)
holes_img = hole_fill(img, k, start_x=100, start_y=100)
#close_img = eros(dilat_img, k)
cv.imshow("Original Image", img)
cv.imshow("Erosion Image", eros_img)
#cv.imshow("Opening Image", open_img)
cv.imshow("Dilation Image", dilat_img)
cv.imshow("Boundary Extraction", bound_img)
cv.imshow("Hole Filling", holes_img)
#cv.imshow("Closing Image", close_img)
cv.waitKey(0)
cv.destroyAllWindows()