from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from windows.add_task import AddTaskWindow
from windows.calendar_window import CalendarWindow
from windows.task_list import TaskListWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ChronoTask")
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()

        title = QLabel("CHRONOTASK")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        quote = QLabel(
            '"Focus on what matters before it becomes urgent."'
        )

        quote.setAlignment(Qt.AlignCenter)

        quote.setStyleSheet("""
            font-size: 18px;
            color: gray;
            font-style: italic;
        """)

        add_btn = QPushButton("Add Task")
        calendar_btn = QPushButton("Calendar")
        task_btn = QPushButton("Task List")
        exit_btn = QPushButton("Exit")

        for btn in [add_btn, calendar_btn, task_btn, exit_btn]:
            btn.setMinimumHeight(45)

        add_btn.clicked.connect(self.open_add)
        calendar_btn.clicked.connect(self.open_calendar)
        task_btn.clicked.connect(self.open_tasks)
        exit_btn.clicked.connect(self.close)

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(15)
        layout.addWidget(quote)
        layout.addSpacing(40)
        layout.addWidget(add_btn)
        layout.addWidget(calendar_btn)
        layout.addWidget(task_btn)
        layout.addWidget(exit_btn)
        layout.addStretch()

        self.setLayout(layout)

    def open_add(self):
        self.window = AddTaskWindow()
        self.window.show()
        self.close()

    def open_calendar(self):
        self.window = CalendarWindow()
        self.window.show()
        self.close()

    def open_tasks(self):
        self.window = TaskListWindow()
        self.window.show()
        self.close()