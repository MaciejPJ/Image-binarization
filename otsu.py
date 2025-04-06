import cv2
import numpy as np

def otsu_binarization(gray_image: np.ndarray) -> np.ndarray:
    """
    Implementation of binarization using Otsu method.

    Args:
        gray_image (np.ndarray): A grayscale image as NumPy array.

    Returns:
        np.ndarray: Binary image after Otsu's algorithm.
    """
    # Check if the image is present
    if gray_image is None:
        raise ValueError("The input image is invalid or could not be loaded.")
    
    # calculate the histogram
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # parameters for algorithm
    total_pixels = gray_image.size
    max_variance = 0
    optimal_threshold = 0

    # Iterate through all possible threshold values
    for i in range(256):
        threshold = i
        sum_intensity_above = 0
        sum_intensity_below = 0
        pixels_above = 0
        pixels_below = 0

        # Perform algorithm's calculations
        for j in range(len(histogram)):
            count = histogram[j][0]
            if j > threshold:
                sum_intensity_above += j * count
                pixels_above += count
            else:
                sum_intensity_below += j * count
                pixels_below += count

        # Calculate mean intensities
        mean_below = sum_intensity_below / pixels_below if pixels_below > 0 else 0
        mean_above = sum_intensity_above / pixels_above if pixels_above > 0 else 0


        # Weights for both classes
        weight_below = pixels_below / total_pixels
        weight_above = pixels_above / total_pixels
    
        # Variance between classes
        between_class_variance = weight_below * weight_above * (mean_below - mean_above) ** 2

        # If needed update the threshold
        if between_class_variance > max_variance:
            max_variance = between_class_variance
            optimal_threshold = threshold

    # Perform the binarization
    thresholded_image = np.where(gray_image < optimal_threshold, 0, 255).astype(np.uint8)

    return thresholded_image