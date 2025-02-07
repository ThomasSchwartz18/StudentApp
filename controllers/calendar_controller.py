from PyQt5.QtWidgets import QWidget
from views.calendar_view import CalendarView
from utils.date_utils import format_date
from utils.file_utils import load_tasks, save_tasks


class CalendarController(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the CalendarController and manages the calendar view and tasks.
        """
        super().__init__(parent)
        self.view = CalendarView(self)
        self.view.calendar.selectionChanged.connect(self.on_date_selected)
        self.view.task_list.taskAdded.connect(self.save_tasks)
        self.view.task_list.taskCompleted.connect(self.save_tasks)
        self.on_date_selected()  # Load tasks for the initial selected date

    def on_date_selected(self):
        """
        Slot triggered when a date is selected in the calendar.
        Loads tasks for the selected date.
        """
        selected_date = self.view.calendar.selectedDate()
        formatted_date = format_date(selected_date.toPyDate())
        self.view.date_label.setText(f"Selected Date: {formatted_date}")

        # Load and display tasks for the selected date
        tasks = load_tasks(formatted_date)
        self.view.task_list.set_tasks(tasks)

    def save_tasks(self):
        """
        Saves the tasks whenever they are added or checked off.
        """
        selected_date = self.view.calendar.selectedDate()
        formatted_date = format_date(selected_date.toPyDate())
        save_tasks(formatted_date, self.view.task_list.get_tasks())
