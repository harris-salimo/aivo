from tkinter import Tk
from typing import NoReturn

from gui import initialize_ui
from menu import setup_menus


def main() -> NoReturn:
    root = Tk()
    root.title("AIVO")
    root.geometry("800x600")
    # root.resizable(width=False, height=False)
    
    initialize_ui(root)
    
    setup_menus(root)
    
    root.mainloop()


if __name__ == "__main__":
    main()
