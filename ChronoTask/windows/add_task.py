from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

from models.task import Task
from data.storage import tasks


class AddTaskWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Task")
        self.setFixedSize(700, 500)

        layout = QFormLayout()

        self.name = QLineEdit()

        self.description = QTextEdit()

        self.deadline = QDateEdit()
        self.deadline.setDate(QDate.currentDate())
        self.deadline.setCalendarPopup(True)

        self.priority = QComboBox()

        self.priority.addItems([
            "Urgent & Important",
            "Urgent & Not Important",
            "Not Urgent & Important",
            "Not Urgent & Not Important"
        ])

        save_btn = QPushButton("Save Task")
        back_btn = QPushButton("Back")

        save_btn.clicked.connect(self.save_task)
        back_btn.clicked.connect(self.go_back)

        layout.addRow("Task Name", self.name)
        layout.addRow("Description", self.description)
        layout.addRow("Deadline", self.deadline)
        layout.addRow("Priority", self.priority)
        layout.addRow(save_btn)
        layout.addRow(back_btn)

        self.setLayout(layout)

    def save_task(self):

        if not self.name.text():

            QMessageBox.warning(
                self,
                "Error",
                "Task name required."
            )
            return

        task = Task(
            self.name.text(),
            self.description.toPlainText(),
            self.deadline.date(),
            self.priority.currentText()
        )

        tasks.append(task)

        QMessageBox.information(
            self,
            "Saved",
            "Task Added Successfully"
        )

        self.name.clear()
        self.description.clear()

    def go_back(self):
        from windows.dashboard import MainWindow

        self.window = MainWindow()
        self.window.show()
        self.close()

