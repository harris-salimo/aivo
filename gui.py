from tkinter import Label, Toplevel, Button, CENTER
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from tkinter import Tk


# Global variables for UI state
label: Optional[Label] = None
current_image: str = ""
opened_image: str = ""


def donothing() -> None:
    """Placeholder function for unimplemented features"""
    filewin = Toplevel()
    button = Button(filewin, text="Do nothing button")
    button.pack()


def close_image() -> None:
    """Close the current image and reset the label"""
    global label
    label.pack_forget()
    label = Label(text="Select an image...", anchor=CENTER)
    label.pack()


def initialize_ui(root: "Tk") -> None:
    """Initialize the main UI components"""
    global label
    
    label = Label(root, text="Select an image...", anchor=CENTER)
    label.pack()
