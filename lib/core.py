import numpy
from typing import Union


def rgb_to_gray(image: numpy.ndarray) -> numpy.ndarray:
    """ Convert colored image to gray level """

    # RGB split using numpy slicing
    _, _ = image.shape[:2]
    blue = image[:, :, 0]
    green = image[:, :, 1] 
    red = image[:, :, 2]
    gray_image = 0.299 * red + 0.587 * green + 0.144 * blue
    gray_image = gray_image.astype(numpy.uint8)

    return gray_image


def rotate(image: numpy.ndarray, angle: Union[int, float]) -> numpy.ndarray:
    """ Rotate an image with an angle """

    image_height, image_width = image.shape[:2]
    # Rotation matrix calculation
    cx, cy = image_width / 2, image_height / 2
    angle_rad = numpy.radians(angle)
    cos_a = numpy.cos(angle_rad)
    sin_a = numpy.sin(angle_rad)
    
    matrix_of_image_pixels = numpy.array([
        [cos_a, -sin_a, cx * (1 - cos_a) + cy * sin_a],
        [sin_a, cos_a, cy * (1 - cos_a) - cx * sin_a]
    ])

    # Affine transformation
    rotated_image = numpy.zeros_like(image)
    
    for i in range(image_height):
        for j in range(image_width):
            # Inverse transformation
            x = matrix_of_image_pixels[0, 0] * j + matrix_of_image_pixels[0, 1] * i + matrix_of_image_pixels[0, 2]
            y = matrix_of_image_pixels[1, 0] * j + matrix_of_image_pixels[1, 1] * i + matrix_of_image_pixels[1, 2]
            
            # Check bounds and interpolate
            if 0 <= x < image_width and 0 <= y < image_height:
                x_int, y_int = int(x), int(y)
                rotated_image[i, j] = image[y_int, x_int]
    
    return rotated_image


def compute_histogram(image: numpy.ndarray) -> numpy.ndarray:
    """ Compute the histogram of an image """

    gray_image = rgb_to_gray(image)
    image_height, image_width = image.shape[:2]

    image_histogram = numpy.zeros(256, int)

    for i in range(0, image_height):
        for j in range(0, image_width):
            image_histogram[gray_image[i][j]] = image_histogram[gray_image[i][j]] + 1

    return image_histogram


def binarize(image: numpy.ndarray, thresh: Union[int, float]) -> numpy.ndarray:
    """ Binarize an image """

    gray_image = rgb_to_gray(image)
    image_height, image_width = image.shape[:2]

    binary_image = gray_image

    for i in range(0, image_height):
        for j in range(0, image_width):
            if gray_image[i][j] < thresh:
                binary_image[i][j] = 0
            else:
                binary_image[i][j] = 255

    return binary_image


def inverse(image: numpy.ndarray) -> numpy.ndarray:
    """ Inverse an image """

    gray_image = rgb_to_gray(image)
    image_height, image_width = image.shape[:2]
    I_MAX = image.max()

    inversed_image = gray_image

    for i in range(0, image_height):
        for j in range(0, image_width):
            inversed_image[i][j] = I_MAX - gray_image[i][j]

    return inversed_image
