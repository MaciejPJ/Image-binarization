import cv2
from otsu import otsu_binarization


# Load image in grayscale
gray_image = cv2.imread("test_image.bmp", cv2.IMREAD_GRAYSCALE)

# Perform Otsu binzrization
binary_image = otsu_binarization(gray_image)

# Display image
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to save the image
# cv2.imwrite("binary_image.bmp", binary_image)