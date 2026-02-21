from matplotlib import pyplot as plt
from PIL import Image
from tkinter import filedialog, Tk

from lib.core import compute_histogram, rgb_to_gray, rotate, binarize, inverse
from lib.convolution import blur, equalize_histogram, stretch_histogram
from lib.morphology import opening, closing, opening_top_hat, closing_top_hat, detect_edge
from lib.utils import apply_image_processing, display_image_array, load_image_as_array
from gui import label, opened_image


def open_image() -> None:
    """Open an image file and display it"""
    global current_image, opened_image

    new_image = filedialog.askopenfilename(initialdir="~/Pictures", title="Open image",
                                           filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))
    
    if new_image:
        if label and label.winfo_exists():
            root = label.winfo_toplevel()
            root.title("{} - AIVO".format(new_image.split("/")[-1]))
        
        current_image = new_image
        opened_image = current_image
        
        image_array = load_image_as_array(new_image)
        display_image_array(image_array, label)


def rotate_an_image(direction: str) -> None:
    """Rotate the current image left or right"""
    angle = 90
    if direction == "RIGHT":
        angle *= -1
    
    apply_image_processing(rotate, angle)


def convert_image_to_gray() -> None:
    """Convert the current image to grayscale"""
    apply_image_processing(rgb_to_gray)


def convert_image_to_binary_image() -> None:
    """Convert the current image to binary (black and white)"""
    apply_image_processing(binarize, 128)


def convert_image_to_inversed_image() -> None:
    """Convert the current image to its negative"""
    apply_image_processing(inverse)


def adjust_image_contraste() -> None:
    """Adjust the contrast of the current image using histogram equalization"""
    apply_image_processing(equalize_histogram)


def adjust_image_luminosity() -> None:
    """Adjust the luminosity of the current image using histogram stretching"""
    apply_image_processing(stretch_histogram, 64, 192)


def blur_an_image() -> None:
    """Apply blur effect to the current image"""
    apply_image_processing(blur)


def extract_edge_on_image() -> None:
    """Detect edges in the current image"""
    apply_image_processing(detect_edge)


def opening_morph_trans_on_image() -> None:
    """Apply morphological opening transformation to the current image"""
    apply_image_processing(opening)


def closing_morph_trans_on_image() -> None:
    """Apply morphological closing transformation to the current image"""
    apply_image_processing(closing)


def oth_morph_trans_on_image() -> None:
    """Apply morphological opening top-hat transformation to the current image"""
    apply_image_processing(opening_top_hat)


def cth_morph_trans_on_image() -> None:
    """Apply morphological closing top-hat transformation to the current image"""
    apply_image_processing(closing_top_hat)


def show_histogram() -> None:
    """Display the histogram of the current image"""
    
    image_array = load_image_as_array(opened_image)
    histogram = compute_histogram(image_array)
    plt.plot(histogram)
    plt.xlabel('Gray level')
    plt.ylabel('Count')
    plt.title("Histogram of the image in gray level")
    plt.show()


def save_image() -> None:
    """Save current image using save_as_image dialog"""
    save_as_image()


def save_as_image() -> None:
    """Save the current image with a chosen filename"""
    global current_image

    image_name = filedialog.asksaveasfilename(defaultextension=".png", initialdir="~/Pictures/", 
                                             title="Save an image", filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg")))

    if image_name:
        image_pil = Image.fromarray(current_image)
        image_pil.save(image_name)
        
        # Get the root window properly
        from gui import label
        if label and label.winfo_exists():
            root = label.winfo_toplevel()
            root.title("{} - AIVO".format(image_name.split("/")[-1]))
