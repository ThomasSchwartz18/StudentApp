# components/shortcut_manager.py
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

def register_shortcut(widget, key_combination, callback):
    """
    Registers a keyboard shortcut on a widget.

    Args:
        widget (QWidget): The widget to attach the shortcut.
        key_combination (str): The key sequence (e.g., "Ctrl+B").
        callback (callable): The function to call when the shortcut is activated.
    """
    shortcut = QShortcut(QKeySequence(key_combination), widget)
    shortcut.activated.connect(callback)
