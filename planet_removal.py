import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg")
img_without_red = img.copy()
img_without_red[:, :, 2] = 0
cv.imshow("Image without red", img_without_red)
img_without_green = img.copy()
img_without_green[:, :, 1] = 0
cv.imshow("Image without green", img_without_green)
img_without_blue = img.copy()
img_without_blue[:, :, 0] = 0
cv.imshow("Image without blue", img_without_blue)
cv.waitKey(0)
cv.destroyAllWindows()