from tkinter import Menu
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tkinter import Tk

from gui import donothing, close_image
from image import (
    open_image, save_image, save_as_image, rotate_an_image, convert_image_to_gray,
    convert_image_to_binary_image, convert_image_to_inversed_image, adjust_image_contraste,
    adjust_image_luminosity, blur_an_image, extract_edge_on_image,
    opening_morph_trans_on_image, closing_morph_trans_on_image,
    oth_morph_trans_on_image, cth_morph_trans_on_image, show_histogram
)


def setup_menus(root: "Tk") -> Menu:
    """Create and configure all menus for the application"""
    
    menubar = Menu(root)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_image)
    filemenu.add_command(label="Save", command=save_image)
    filemenu.add_command(label="Save as", command=save_as_image)
    filemenu.add_command(label="Close", command=close_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_command(label="Redo", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    
    imagemenu = Menu(menubar, tearoff=0)
    imagemenu.add_command(label="Flip Horizontally", command=donothing)
    imagemenu.add_command(label="Flip Vertically", command=donothing)
    imagemenu.add_command(label="Rotate Right", command=lambda: rotate_an_image("RIGHT"))
    imagemenu.add_command(label="Rotate Left", command=lambda: rotate_an_image("LEFT"))
    imagemenu.add_command(label="Adjust contraste", command=adjust_image_contraste)
    imagemenu.add_command(label="Adjust luminosity", command=adjust_image_luminosity)
    imagemenu.add_command(label="Gray color", command=convert_image_to_gray)
    imagemenu.add_command(label="BW color", command=convert_image_to_binary_image)
    imagemenu.add_command(label="Negative color", command=convert_image_to_inversed_image)
    imagemenu.add_command(label="Blur image", command=blur_an_image)
    imagemenu.add_command(label="Edge detect", command=extract_edge_on_image)
    imagemenu.add_command(label="Morph Trans Opening", command=opening_morph_trans_on_image)
    imagemenu.add_command(label="Morph Trans Closing", command=closing_morph_trans_on_image)
    imagemenu.add_command(label="Morph Trans OTH", command=oth_morph_trans_on_image)
    imagemenu.add_command(label="Morph Trans CTH", command=cth_morph_trans_on_image)
    imagemenu.add_command(label="Voir l'histogramme", command=show_histogram)
    menubar.add_cascade(label="Image", menu=imagemenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=donothing)
    helpmenu.add_command(label="About", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    root.config(menu=menubar)
    
    return menubar
