import numpy as np
import cv2 as cv
mat = np.zeros((16, 16), dtype=np.uint8)
val = 0
for i in range(16):
    for j in range(16):
        mat[i][j] = val
        val += 1
def custom_contrast_stretching(pix_val):
    if pix_val == 0:
        return 255
    elif 0 < pix_val <= 100:
        return int(-0.55 * pix_val + 255)
    elif 100 < pix_val <= 150:
        return int(-3 * pix_val + 500)
    elif 150 < pix_val < 255:
        return int(-0.477 * pix_val + 121.428)
    else:
        return 0
out_mat = np.zeros((16, 16), dtype=np.uint8)
for x in range(16):
    for y in range(16):
        out_mat[x][y] = custom_contrast_stretching(mat[x][y])
cv.imwrite('C:\Dev\DIP\Open CV\photos\Lenna.png', out_mat)
cv.imshow('C:\Dev\DIP\Open CV\photos\Lenna.png', out_mat)
cv.waitKey(0)
cv.destroyAllWindows()


