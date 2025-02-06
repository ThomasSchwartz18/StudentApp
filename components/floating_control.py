from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize

class FloatingControl(QWidget):
    """
    A floating control widget that sits in the bottom-left corner.
    Initially, it displays an image as the toggle button. When clicked, it grows
    vertically with straight sides but circular top and bottom, revealing the
    calendar, notes, and home buttons inside the expanded circle, moving upwards.
    The image (home-64.png) stays static while everything else functions as expected.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.expanded = False
        self.init_ui()

    def init_ui(self):
        # Set up a vertical layout with no margins or spacing.
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        # Create the calendar, notes, and home buttons (initially hidden) and scale them down.
        button_size = 30  # Scale down the button size
        self.btn_calendar = QPushButton("📅", self)  # Calendar button with emoji
        self.btn_notes = QPushButton("📝", self)     # Notes button with emoji
        self.btn_home = QPushButton("🏠", self)      # Home button with emoji
        for btn in (self.btn_calendar, self.btn_notes, self.btn_home):
            btn.setFixedSize(button_size, button_size)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #c9c3be;
                    color: white;
                    border: none;
                    border-radius: 15px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #a6a19d;
                }
            """)
            btn.hide()

        # Create the main toggle label (the image as the label).
        self.label_toggle = QLabel(self)
        self.label_toggle.setFixedSize(50, 50)  # Set the size of the label to match the image

        # Load the image and scale it down to 30x30
        pixmap = QPixmap("resources/images/home-64.png")  # Load the image
        self.label_toggle.setPixmap(pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_toggle.setAlignment(Qt.AlignCenter)

        # Set the background of the label to transparent to avoid the blue box.
        self.label_toggle.setStyleSheet("background: transparent;")
        self.label_toggle.setAlignment(Qt.AlignCenter)

        # Connect the toggle label to expand/collapse.
        self.label_toggle.mousePressEvent = self.toggle_expand

        # Connect the calendar, notes, and home buttons to their respective actions.
        self.btn_calendar.clicked.connect(self.show_calendar)
        self.btn_notes.clicked.connect(self.show_notes)
        self.btn_home.clicked.connect(self.go_home)

        # Add the buttons and label to the layout in reverse order to make them appear above the toggle label.
        self.layout.addWidget(self.btn_calendar, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.btn_notes, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.btn_home, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_toggle, alignment=Qt.AlignCenter)

        # Set the initial size of the widget to match the toggle label.
        self.resize(50, 50)  # Use resize instead of setFixedSize.

        # Create the animation for expanding and collapsing.
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(300)  # Animation duration in milliseconds.
        self.animation.valueChanged.connect(self.update_position_and_style)  # Update position and style during animation.

    def paintEvent(self, event):
        """
        Override the paint event to draw a circle around the image.
        """
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Change the pen color to match the button color
        pen = QPen(QColor(201, 195, 190))  # Set color to #c9c3be (button color)
        pen.setWidth(2)  # Set the thickness of the border
        painter.setPen(pen)

        # Calculate the position of the label_toggle within the FloatingControl widget
        label_pos = self.label_toggle.pos()
        label_size = self.label_toggle.size()

        # Draw a circle around the label_toggle
        painter.drawEllipse(label_pos.x() + 2, label_pos.y() + 2, label_size.width() - 4, label_size.height() - 4)
        painter.end()

    def toggle_expand(self, event):
        if self.expanded:
            self.collapse()
        else:
            self.expand()

    def expand(self):
        # Calculate the expanded height (height of all buttons + spacing).
        expanded_height = (
            self.label_toggle.height() +
            self.btn_calendar.height() +
            self.btn_notes.height() +
            self.btn_home.height() +
            15  # Additional spacing for the new button
        )
        self.animation.setStartValue(self.size())
        self.animation.setEndValue(QSize(50, expanded_height))
        self.animation.start()
        self.expanded = True

    def collapse(self):
        self.animation.setStartValue(self.size())
        self.animation.setEndValue(QSize(50, 50))
        self.animation.start()
        self.expanded = False

    def update_position_and_style(self):
        """
        Dynamically updates the widget's position and style during the animation.
        """
        # Update the widget's position to move upwards as it expands.
        if self.parent():
            parent_height = self.parent().height()      
            margin = 25  # Distance from the bottom.
            y = parent_height - self.height() - margin  # Adjust y position to move upwards.
            self.move(self.x(), y)

        # Update the widget's style to maintain a circular top and bottom.
        height = self.height()
        radius = height / 2  # Radius for circular top and bottom.
        self.setStyleSheet(f"""
            QWidget {{
                background-color: #3498DB;
                border: none;
                border-radius: {radius}px;
            }}
        """)

        # Show or hide buttons based on the animation progress.
        if height > 90:  # Threshold to reveal buttons (increased for the new button).
            self.btn_calendar.show()
            self.btn_notes.show()
            self.btn_home.show()
        else:
            self.btn_calendar.hide()
            self.btn_notes.hide()
            self.btn_home.hide()

        # Ensure the label_toggle is always visible and centered.
        self.label_toggle.show()

    def show_calendar(self):
        """
        Triggers the calendar view in the main window.
        """
        if self.parent():
            self.parent().show_calendar()

    def show_notes(self):
        """
        Triggers the notes view in the main window.
        """
        if self.parent():
            self.parent().show_notes()

    def go_home(self):
        """
        Triggers the dashboard home view in the main window.
        """
        if self.parent():
            self.parent().go_home()  # Ensure the parent has a `go_home` method.