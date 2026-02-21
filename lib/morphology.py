import numpy

from .core import binarize
from .utils import is_valid_pixel


def _dilate_pixel(image: numpy.ndarray, kernel: numpy.ndarray, x: int, y: int) -> int:
    """ Apply dilation logic for a single pixel """
    kernel_half_width = kernel.shape[0] // 2
    kernel_half_height = kernel.shape[1] // 2
    
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            x_image = x + i - kernel_half_width
            y_image = y + j - kernel_half_height
            
            if is_valid_pixel(image, x_image, y_image):
                if image[x_image, y_image] and kernel[i, j]:
                    return 255
    return 0


def _erode_pixel(image: numpy.ndarray, kernel: numpy.ndarray, x: int, y: int) -> int:
    """ Apply erosion logic for a single pixel """
    kernel_half_width = kernel.shape[0] // 2
    kernel_half_height = kernel.shape[1] // 2
    
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            x_image = x + i - kernel_half_width
            y_image = y + j - kernel_half_height
            
            if is_valid_pixel(image, x_image, y_image):
                if kernel[i, j] and not (image[x_image, y_image]):
                    return 0
    return 255


def dilatation(binary_image: numpy.ndarray) -> numpy.ndarray:
    """ Dilate a binary image """
    kernel = numpy.ones((3, 3), dtype=numpy.uint8)
    dilated_image = numpy.zeros(binary_image.shape, dtype=numpy.uint8)
    
    for x in range(binary_image.shape[0]):
        for y in range(binary_image.shape[1]):
            dilated_image[x, y] = _dilate_pixel(binary_image, kernel, x, y)
    
    return dilated_image


def erosion(binary_image: numpy.ndarray) -> numpy.ndarray:
    """ Erode a binary image """
    kernel = numpy.ones((3, 3), dtype=numpy.uint8)
    eroded_image = numpy.zeros(binary_image.shape, dtype=numpy.uint8)
    
    for x in range(binary_image.shape[0]):
        for y in range(binary_image.shape[1]):
            eroded_image[x, y] = _erode_pixel(binary_image, kernel, x, y)
    
    return eroded_image


def opening(image: numpy.ndarray) -> numpy.ndarray:
    """ Apply dilatation just after erosion operation
    to an image which need to be binarizing first """

    binarized_image = binarize(image, 128)

    return dilatation(erosion(binarized_image))


def closing(image: numpy.ndarray) -> numpy.ndarray:
    """ Apply erosion just after dilatation operation
    to an image which need to be binarizing first """

    binarized_image = binarize(image, 128)

    return erosion(dilatation(binarized_image))


def opening_top_hat(image: numpy.ndarray) -> numpy.ndarray:
    """ Apply opening top hat transform """
    binary_image = binarize(image, 128)

    return binary_image - opening(image)


def closing_top_hat(image: numpy.ndarray) -> numpy.ndarray:
    """ Apply closing top hat transform """
    binary_image = binarize(image, 128)

    return closing(image) - binary_image


def detect_edge(image: numpy.ndarray) -> numpy.ndarray:
    """ Detect edge on an image """

    binary_image = binarize(image, 128)

    image_after_dilatation = dilatation(binary_image)
    image_after_dilatation = binary_image - image_after_dilatation

    image_after_erosion = erosion(binary_image)
    image_after_erosion = binary_image - image_after_erosion

    return image_after_dilatation + image_after_erosion
