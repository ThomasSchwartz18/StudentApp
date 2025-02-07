from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton, QListWidgetItem
from PyQt5.QtCore import pyqtSignal


class TaskList(QWidget):
    """
    A task list component that allows users to add and check off tasks.
    """
    taskAdded = pyqtSignal()
    taskCompleted = pyqtSignal()

    def __init__(self, parent=None):
        """
        Initializes the task list UI.
        """
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """
        Sets up the task list UI.
        """
        layout = QVBoxLayout(self)

        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        layout.addWidget(self.task_input)

        self.add_task_button = QPushButton("Add Task", self)
        self.add_task_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_button)

        self.setLayout(layout)

    def add_task(self):
        """
        Adds a new task to the task list.
        """
        task_text = self.task_input.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            self.task_list.addItem(item)
            self.task_input.clear()
            self.taskAdded.emit()

    def set_tasks(self, tasks):
        """
        Sets the tasks for the selected date.
        """
        self.task_list.clear()
        for task in tasks:
            item = QListWidgetItem(task)
            self.task_list.addItem(item)

    def get_tasks(self):
        """
        Returns a list of tasks currently displayed.
        """
        return [self.task_list.item(i).text() for i in range(self.task_list.count())]
