# utils/ui_helpers.py
from PyQt5.QtWidgets import QPushButton, QLabel

def set_window_default_background(widget):
    """
    Sets the default background color and global font properties for the given widget.
    
    This replicates the global CSS rules:
      - background-color: #f9f9f9;
      - font-family: Arial;
      - font-size: 14px;
    
    Args:
        widget (QWidget): The widget (e.g., a window) to style.
    """
    global_style = "background-color: #f9f9f9; font-family: Arial; font-size: 14px;"
    widget.setStyleSheet(global_style)

def create_button(parent, text, command, **options):
    """
    Creates a standardized QPushButton with inline QSS that mimics the following CSS:
    
    QPushButton {
        background-color: #9C8676;
        color: white;
        border: none;
        padding: 0px;
        border-radius: 0px;
        font-size: 14px;
        font-family: Arial;
    }
    
    QPushButton:hover {
        background-color: #C3A793;
    }
    
    You can override any of these properties by passing keyword arguments. For example:
      create_button(parent, "Click Me", callback, background_color="#123456", hover={"background-color": "#654321"})
    
    Note: In Python keyword arguments use underscores instead of hyphens. They will be
    converted to hyphenated CSS property names.
    
    Args:
        parent (QWidget): The parent widget.
        text (str): The button label.
        command (callable): The function to execute on button click.
        **options: Additional styling options to override defaults. To override hover styles,
                   pass a dictionary using the key 'hover'.
    
    Returns:
        QPushButton: The created button with the defined styling.
    """
    button = QPushButton(text, parent)
    
    # Default normal state style as a dictionary.
    normal_default = {
        # "background-color": "#9C8676",
        "color": "black",
        "border": "none",
        "padding": "0px",
        "border-radius": "0px",
        "font-size": "14px",
        "font-family": "Arial",
        "border": "none",  # Clear any default borders.
        "border-bottom": "2px solid #9C8676"  # Only bottom border.
    }
    # Default hover style.
    hover_default = {
        "background-color": "#c9c3be"
    }
    
    # Extract hover options if provided.
    hover_options = options.pop("hover", {})
    
    # Convert Python-style keys (with underscores) to CSS keys (with hyphens).
    def convert_keys(style_dict):
        return {k.replace("_", "-"): v for k, v in style_dict.items()}
    
    normal_override = convert_keys(options)
    hover_override = convert_keys(hover_options)
    
    # Merge default styles with any overrides (overrides take precedence).
    normal_style = {**normal_default, **normal_override}
    hover_style = {**hover_default, **hover_override}
    
    # Convert the style dictionaries into CSS strings.
    normal_style_string = "; ".join(f"{k}: {v}" for k, v in normal_style.items())
    hover_style_string = "; ".join(f"{k}: {v}" for k, v in hover_style.items())
    
    # Construct the final QSS style.
    style = f"QPushButton {{ {normal_style_string}; }} QPushButton:hover {{ {hover_style_string}; }}"
    button.setStyleSheet(style)
    button.clicked.connect(command)
    return button

def create_label(parent, text, **options):
    """
    Creates a standardized QLabel with inline styling equivalent to:
    
    QLabel {
        font-size: 14px;
        color: #333;
        font-family: Arial;
    }
    
    Extra styling options can be provided as keyword arguments. For example:
      create_label(parent, "Title", font_size="18px", color="#000")
    
    Note: Use underscores in place of hyphens in property names.
    
    Args:
        parent (QWidget): The parent widget.
        text (str): The text to display.
        **options: Additional styling options.
    
    Returns:
        QLabel: The created label with the defined styling.
    """
    label = QLabel(text, parent)
    
    # Default label style.
    default_style = {
        "font-size": "14px",
        "color": "#333",
        "font-family": "Arial"
    }
    
    # Convert keyword arguments from underscores to hyphens.
    def convert_keys(style_dict):
        return {k.replace("_", "-"): v for k, v in style_dict.items()}
    
    override_style = convert_keys(options)
    
    # Merge the default style with any overrides.
    combined_style = {**default_style, **override_style}
    style_string = "; ".join(f"{k}: {v}" for k, v in combined_style.items())
    label.setStyleSheet(style_string)
    return label
