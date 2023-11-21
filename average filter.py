import numpy as np
import cv2 as cv
def custom_img_smooth(img, kernel_size):
    h, w, channels = img.shape
    smooth_img = np.zeros_like(img)
    kernel_r_x, kernel_r_y = kernel_size[0] // 2, kernel_size[1] // 2
    for y in range(h):
        for x in range(w):
            avg_color = [0, 0, 0]
            count = 0
            for ky in range(-kernel_r_y, kernel_r_y + 1):
                for kx in range(-kernel_r_x, kernel_r_x + 1):
                    pix_x = x + kx
                    pix_y = y + ky
                    if 0 <= pix_x < w and 0 <= pix_y < h:
                        avg_color += img[pix_y, pix_x]
                        count += 1
            avg_color //= count
            smooth_img[y, x] = avg_color
    return smooth_img
def main():
    img = cv.imread('C:\Dev\DIP\Open CV\photos\Lenna.png')
    kernel_size = (5, 5)
    smooth_img = custom_img_smooth(img, kernel_size)
    cv.imwrite('C:\Dev\DIP\Open CV\photos\IMG20200821113912.jpg', smooth_img)
    cv.imshow('Original Image', img)
    cv.imshow('Custom Smoothed Image', smooth_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()
