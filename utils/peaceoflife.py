def gui_supported() -> bool:
    import tkinter as tk
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        root.update_idletasks()  # Update the GUI (optional)
        return True
    except tk.TclError:
        return False


def select_folder_gui() -> str:
    import tkinter as tk
    from tkinter import filedialog

    from utils.configuring import save_destination

    root = tk.Tk()
    root.withdraw()

    destination = filedialog.askdirectory(title="Select Destination Folder")

    save_destination(destination)


def get_destination_folder_gui() -> str:
    from utils.configuring import load_destination
    destination = load_destination()
    if destination == None or destination == "":
        if gui_supported():
            select_folder_gui()
            return load_destination()
        

def sanatize_input(input: str) -> str:
    from re import sub
    
    invalid_chars = r'[<>:"/\\|?*]'
    
    sanitized = sub(invalid_chars, '', input)
    
    sanitized = sanitized.strip()

    max_length = 255
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized