# utils/resource_loader.py
from PyQt5.QtGui import QPixmap

def load_image(path, size=None):
    """
    Loads an image from the specified path and optionally resizes it.
    
    Args:
        path (str): The path to the image file.
        size (tuple, optional): A tuple (width, height) to resize the image.
        
    Returns:
        QPixmap: The loaded image as a QPixmap.
    """
    pixmap = QPixmap(path)
    if size:
        pixmap = pixmap.scaled(size[0], size[1])
    return pixmap

def load_stylesheet(path):
    """
    Loads a stylesheet (CSS/QSS file) from the specified path.
    
    Args:
        path (str): The path to the stylesheet file.
        
    Returns:
        str: The content of the stylesheet.
    """
    try:
        with open(path, 'r') as file:
            stylesheet = file.read()
        return stylesheet
    except Exception as e:
        print(f"Failed to load stylesheet: {e}")
        return ""
