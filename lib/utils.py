import numpy
from PIL import Image, ImageTk
from tkinter import Label
from typing import Callable, Any

import gui


def is_valid_pixel(image: numpy.ndarray, x: int, y: int) -> bool:
    """Check if pixel coordinates are within image bounds"""
    return (x >= 0 and x < image.shape[0] and 
            y >= 0 and y < image.shape[1])


def load_image_as_array(image_path: str) -> numpy.ndarray:
    """Load an image file and return as numpy array"""
    image_pil = Image.open(image_path)
    return numpy.array(image_pil)


def display_image_array(image_array: numpy.ndarray, label_widget: Label) -> None:
    """Display an image array in GUI label"""
    if label_widget is None:
        return
        
    image = ImageTk.PhotoImage(Image.fromarray(image_array))
    
    label_widget.pack_forget()
    new_label = Label(image=image, anchor="center")
    new_label.image = image
    new_label.pack()
    
    # Update the global label reference
    gui.label = new_label


def update_current_image(image_array: numpy.ndarray, label_widget: Label) -> None:
    """Update current image and display it"""
    global current_image
    current_image = image_array
    display_image_array(image_array, label_widget)


def apply_image_processing(process_func: Callable[[numpy.ndarray, Any], numpy.ndarray], *args, **kwargs) -> None:
    """Apply image processing function to current image"""
    global current_image, opened_image
    
    if current_image is None:
        return
        
    image_pil = Image.open(opened_image)
    image_array = numpy.array(image_pil)
    new_image = process_func(image_array, *args, **kwargs)
    
    # Get the label from gui module
    display_image_array(new_image, gui.label)
    current_image = new_image
