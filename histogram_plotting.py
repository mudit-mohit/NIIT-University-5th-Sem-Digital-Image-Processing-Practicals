import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("C:\Dev\DIP\Open CV\photos\IMG20200821113912.jpg")
b, g, r = cv.split(img)
plt.figure(figsize=(10, 6))
plt.hist(b.ravel(), 256, [0, 256], color="b", label="Blue")
plt.hist(g.ravel(), 256, [0, 256], color="g", label="Green")
plt.hist(r.ravel(), 256, [0, 256], color="r", label="Red")
plt.title("Histogram for Color Scale Picture")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.legend()
plt.show()