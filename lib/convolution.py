import numpy
from typing import Union

from .core import rgb_to_gray
from .utils import is_valid_pixel


def _apply_convolution(image: numpy.ndarray, kernel: numpy.ndarray) -> numpy.ndarray:
    """ Apply convolution kernel to image """
    new_image = numpy.zeros(image.shape, dtype=numpy.uint8)
    
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            new_image[x, y] = _compute_convolution_pixel(image, kernel, x, y)
    
    return new_image


def _compute_convolution_pixel(image: numpy.ndarray, kernel: numpy.ndarray, x: int, y: int) -> Union[int, float]:
    """ Compute convolution value for a single pixel """
    kernel_half_width = kernel.shape[0] // 2
    kernel_half_height = kernel.shape[1] // 2
    pixel_value = 0
    
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            x_image = x + i - kernel_half_width
            y_image = y + j - kernel_half_height
            
            if is_valid_pixel(image, x_image, y_image):
                pixel_value += kernel[i, j] * image[x_image, y_image]
    
    return pixel_value


def blur(image: numpy.ndarray) -> numpy.ndarray:
    """ Blur an image """
    gray_image = rgb_to_gray(image)
    filter_size = 7
    kernel = (1 / (filter_size * filter_size)) * numpy.ones((filter_size, filter_size), dtype=numpy.uint8)
    
    return _apply_convolution(gray_image, kernel)


def equalize_histogram(image: numpy.ndarray) -> numpy.ndarray:
    """ Equalize the histogram of an image """

    gray_image = rgb_to_gray(image)
    image_height, image_width = image.shape[:2]
    histogram = numpy.zeros(256, int)

    for i in range(0, image_width):
        for j in range(0, image_height):
            histogram[gray_image[i][j]] = histogram[gray_image[i][j]] + 1

    histogram_cumulated = numpy.zeros(256, int)
    histogram_cumulated[0] = histogram[0]
    for i in range(1, 256):
        histogram_cumulated[i] = histogram[i] + histogram_cumulated[i - 1]

    number_of_pixels = gray_image.size
    hist0c = histogram_cumulated / number_of_pixels * 255

    for i in range(0, gray_image.shape[0]):
        for j in range(0, gray_image.shape[1]):
            gray_image[i][j] = hist0c[gray_image[i][j]]

    # Grayscale to BGR conversion
    height, width = gray_image.shape
    result_image = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    
    for i in range(height):
        for j in range(width):
            gray_value = gray_image[i, j]
            result_image[i, j] = [gray_value, gray_value, gray_value]
    
    return result_image


def stretch_histogram(image: numpy.ndarray, min: Union[int, float], max: Union[int, float]) -> numpy.ndarray:
    """ Stretch the histogram of an image """

    gray_image = rgb_to_gray(image)
    image_height, image_width = image.shape[:2]

    for i in range(0, image_width):
        for j in range(0, image_height):
            gray_image[i][j] = (255 * (gray_image[i][j] - min)) / (max - min)

    # Grayscale to BGR conversion
    height, width = gray_image.shape
    result_image = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    
    for i in range(height):
        for j in range(width):
            gray_value = gray_image[i, j]
            result_image[i, j] = [gray_value, gray_value, gray_value]
    
    return result_image
