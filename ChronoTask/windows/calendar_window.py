from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from data.storage import tasks


class CalendarWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar")
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()

        self.task_list = QListWidget()

        self.highlight_dates()

        self.calendar.clicked.connect(
            self.show_tasks_for_date
        )

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)

        layout.addWidget(self.calendar)

        layout.addWidget(
            QLabel("Tasks on Selected Date:")
        )

        layout.addWidget(self.task_list)

        layout.addWidget(back_btn)

        self.setLayout(layout)

    def highlight_dates(self):

        fmt = QTextCharFormat()

        fmt.setBackground(
            QColor("#FFD54F")
        )

        fmt.setFontWeight(QFont.Bold)

        for task in tasks:
            self.calendar.setDateTextFormat(
                task.deadline,
                fmt
            )

    def show_tasks_for_date(self, date):

        self.task_list.clear()

        found = False

        for task in tasks:

            if task.deadline == date:

                self.task_list.addItem(
                    f"{task.name} | {task.priority} | {task.progress}%"
                )

                found = True

        if not found:

            self.task_list.addItem(
                "No tasks scheduled."
            )

    def go_back(self):

        from windows.dashboard import MainWindow

        self.window = MainWindow()
        self.window.show()
        self.close()