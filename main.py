import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from utils.resource_loader import load_stylesheet  # Utility for loading stylesheets
import config  # Application configuration constants
from components.floating_control import FloatingControl  # Import the floating control widget
from components.custom_title_bar import CustomTitleBar  # Import the custom title bar widget

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
                    stop: 0 rgba(255, 245, 230, 200),  /* Very light tan (almost white) with transparency */
                    stop: 0.5 rgba(255, 245, 230, 150),  /* Very light tan (almost white) with transparency */
                    stop: 1 rgba(255, 245, 230, 100)  /* Very light tan (almost white) with transparency */
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

        # Add the custom title bar
        self.title_bar = CustomTitleBar(self)
        self.layout.addWidget(self.title_bar)

        # Connect the close signal from the title bar to the close method
        self.title_bar.close_signal.connect(self.close)

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
        Repositions the floating control widget to the bottom-left corner on window resize.
        """
        self.update_floating_control_position()
        super().resizeEvent(event)

    def update_floating_control_position(self):
        """
        Update the position of the floating control widget based on the window size.
        It is placed in the bottom-left corner with a 20px margin from the edges.
        """
        margin = 20  # Distance from the window edges
        vertical_offset = 20 # Distance from the bottom to move the floating widget higher
        
        # Ensure the floating control widget size is fully calculated
        self.floating_control.adjustSize()

        # Calculate the new x and y position
        x = margin  # Position on the left side
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
        if self.layout.count() > 1:  # Check if there's more than just the title bar
            current_view = self.layout.itemAt(1).widget()
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
        if self.layout.count() > 1:  # Check if there's more than just the title bar
            current_view = self.layout.itemAt(1).widget()
            self.view_history.append(current_view)
            current_view.hide()
            self.layout.removeWidget(current_view)
        self.layout.addWidget(view_widget)
        view_widget.show()
        
    def show_calendar(self):
        """
        Displays the Calendar view in the right section.
        """
        self.dashboard_view.show_calendar()

    def show_notes(self):
        """
        Displays the Notes view in the right section.
        """
        self.dashboard_view.show_notes()
        
    def go_home(self):
        """
        Resets the view to the dashboard home.
        """
        self.dashboard_view.go_back()  # Assuming `go_back` resets the view to the home screen.
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Optionally, load an external stylesheet if needed.
    stylesheet = load_stylesheet("resources/styles.css")
    app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())