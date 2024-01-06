import numpy as np
import cv2 as cv
def rgb_to_hsi(rgb):
    r, g, b = rgb / 255.0
    intensity = (r + g + b) / 3.0
    min_rgb = min(r, g, b)
    saturation = 1 - 3 * min_rgb / (r + g + b) if (r + g + b) != 0 else 0
    numerator = 0.5 * ((r - g) + (r - b))
    denominator = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
    angle = np.arccos(numerator / (denominator + 1e-10))
    hue = angle if b <= g else 2 * np.pi - angle
    hue = np.degrees(hue)
    return hue, saturation, intensity
if __name__ == "__main__":
    input_image = cv.imread("C:\Dev\DIP\Open CV\photos\IMG20200821113904.jpg", cv.IMREAD_COLOR)
    hue_image = np.zeros_like(input_image[:, :, 0], dtype=np.uint8)
    saturation_image = np.zeros_like(input_image[:, :, 0], dtype=np.uint8)
    intensity_image = np.zeros_like(input_image[:, :, 0], dtype=np.uint8)
for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            rgb_values = input_image[i, j]
            hsi_values = rgb_to_hsi(rgb_values)
            hue_image[i, j] = hsi_values[0]
            saturation_image[i, j] = hsi_values[1] * 255
            intensity_image[i, j] = hsi_values[2] * 255
cv.imshow("Input Image", input_image)
cv.imshow("Hue Image", hue_image)
cv.imshow("Saturation Image", saturation_image)
cv.imshow("Intensity Image", intensity_image)
cv.waitKey(0)
cv.destroyAllWindows()