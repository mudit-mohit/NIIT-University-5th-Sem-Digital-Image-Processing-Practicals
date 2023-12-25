import cv2 as cv
img = cv.imread("C:\Dev\DIP\Open CV\photos\Lenna.png")
b, g, r = cv.split(img)
cv.imshow("Original Image", img)
cv.imshow("Blue Channel", b)
cv.imshow("Green Channel", g)
cv.imshow("Red Channel", r)
cv.waitKey(0)
cv.destroyAllWindows()
