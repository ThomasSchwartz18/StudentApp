# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from utils.resource_loader import load_stylesheet  # Utility for loading stylesheets
import config  # Application configuration constants
from components.floating_control import FloatingControl  # Import the floating control widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title and dimensions from config.
        self.setWindowTitle(config.APP_TITLE)
        self.setGeometry(100, 100, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

        # Enable translucency and remove the window frame for a glossy, transparent look.
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Create the central widget with a glossy, transparent gradient style.
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 rgba(255, 255, 255, 200),
                    stop: 0.5 rgba(255, 255, 255, 150),
                    stop: 1 rgba(255, 255, 255, 100)
                );
                border: 1px solid rgba(255, 255, 255, 100);
                border-radius: 10px;
            }
        """)
        self.setCentralWidget(self.central_widget)

        # Create a layout for hosting our views without extra padding.
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Maintain a history of views for navigation.
        self.view_history = []
        self.load_dashboard_view()

        # Create and add the floating control widget. It remains visible on all screens.
        self.floating_control = FloatingControl(self)
        self.floating_control.show()

        # Position the floating control widget after it's shown.
        self.update_floating_control_position()

    def resizeEvent(self, event):
        """
        Repositions the floating control widget to the bottom-right corner on window resize.
        """
        self.update_floating_control_position()
        super().resizeEvent(event)

    def update_floating_control_position(self):
        """
        Update the position of the floating control widget based on the window size.
        It is placed in the bottom-right corner with a 100px margin from the bottom edge.
        """
        margin = 20  # Distance from the right side
        vertical_offset = 100  # Distance from the bottom to move the floating widget higher

        # Ensure the floating control widget size is fully calculated
        self.floating_control.adjustSize()

        # Calculate the new x and y position
        x = self.width() - self.floating_control.width() - margin  # Right side
        y = self.height() - self.floating_control.height() - margin - vertical_offset  # Bottom side adjusted upwards

        # Set the new position of the floating control widget
        self.floating_control.move(x, y)

    def mousePressEvent(self, event):
        """
        Detects mouse clicks in the application window.
        If clicked outside the floating control, collapse the control to its circle.
        """
        if not self.floating_control.rect().contains(self.floating_control.mapFromGlobal(event.globalPos())):
            self.floating_control.collapse()
        super().mousePressEvent(event)

    def load_dashboard_view(self):
        """
        Creates and displays the Dashboard view.
        """
        if self.layout.count() > 0:
            current_view = self.layout.itemAt(0).widget()
            self.view_history.append(current_view)
            current_view.deleteLater()
        from views.dashboard_view import DashboardView  # Import here to avoid circular dependencies.
        self.dashboard_view = DashboardView(self)
        self.layout.addWidget(self.dashboard_view)

    def navigate_to(self, view_widget):
        """
        Switches from the current view to a new view.

        Args:
            view_widget (QWidget): The new view widget to display.
        """
        if self.layout.count() > 0:
            current_view = self.layout.itemAt(0).widget()
            self.view_history.append(current_view)
            current_view.hide()
            self.layout.removeWidget(current_view)
        self.layout.addWidget(view_widget)
        view_widget.show()

    def resizeEvent(self, event):
        """
        Repositions the floating control widget to the bottom-left corner on window resize.
        """
        margin = 20  # Distance from the window edges.
        x = margin  # Position on the left side.
        y = self.height() - self.floating_control.height() - margin
        self.floating_control.move(x, y)
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        """
        Detects mouse clicks in the application window.
        If clicked outside the floating control, collapse the control to its circle.
        """
        if not self.floating_control.rect().contains(self.floating_control.mapFromGlobal(event.globalPos())):
            self.floating_control.collapse()
        super().mousePressEvent(event)
        
    def label_toggle_mousePressEvent(self, event):
        """Start dragging the main window if clicking and holding on the floating image."""
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.globalPos() - self.parent().frameGeometry().topLeft()
            event.accept()

    def label_toggle_mouseMoveEvent(self, event):
        """Move the main application window when dragging the floating control."""
        if self.is_dragging:
            new_position = event.globalPos() - self.offset
            self.parent().move(new_position)
            event.accept()

    def label_toggle_mouseReleaseEvent(self, event):
        """Stop dragging when the mouse is released."""
        self.is_dragging = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Optionally, load an external stylesheet if needed.
    stylesheet = load_stylesheet("resources/styles.css")
    app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
