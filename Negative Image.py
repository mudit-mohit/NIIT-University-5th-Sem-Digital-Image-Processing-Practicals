import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg', cv2.IMREAD_GRAYSCALE)
neg_img = 255 - img
plt.imshow(neg_img, cmap='gray')
plt.title('Negative Image')
plt.axis('off')
plt.show()
