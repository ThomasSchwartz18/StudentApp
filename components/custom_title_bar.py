from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent

class CustomTitleBar(QWidget):
    # Signal to be emitted when the window needs to be closed
    close_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)  # Set the height of the title bar
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #D8DEE9;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                color: #D8DEE9;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #4C566A;
            }
        """)

        # Layout for the title bar
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 5, 0)
        layout.setSpacing(5)

        # Title label
        self.title_label = QLabel("App")
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.title_label)

        # Spacer to push buttons to the right
        layout.addStretch()

        # Minimize button
        self.minimize_button = QPushButton("─")
        self.minimize_button.clicked.connect(self.minimize_window)
        layout.addWidget(self.minimize_button)

        # Close button
        self.close_button = QPushButton("✕")
        self.close_button.clicked.connect(self.close_signal.emit)
        layout.addWidget(self.close_button)

        # Variables for dragging the window
        self.dragging = False
        self.offset = None

    def minimize_window(self):
        """Minimize the main window."""
        self.window().showMinimized()

    def mousePressEvent(self, event: QMouseEvent):
        """Handle mouse press event to start dragging the window."""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.window().pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        """Handle mouse move event to drag the window."""
        if self.dragging and self.offset is not None:
            self.window().move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Handle mouse release event to stop dragging the window."""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.offset = None