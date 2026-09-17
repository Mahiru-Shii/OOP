from PyQt5.QtWidgets import *

from data.storage import tasks


class TaskListWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task List")
        self.setFixedSize(900, 500)

        layout = QVBoxLayout()

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Task",
            "Deadline",
            "Priority",
            "Progress"
        ])

        self.table.horizontalHeader().setStretchLastSection(True)

        self.load_tasks()

        update_btn = QPushButton("Update Progress")
        back_btn = QPushButton("Back")

        update_btn.clicked.connect(
            self.open_progress
        )

        back_btn.clicked.connect(
            self.go_back
        )

        layout.addWidget(self.table)
        layout.addWidget(update_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def load_tasks(self):

        self.table.setRowCount(len(tasks))

        for row, task in enumerate(tasks):

            self.table.setItem(
                row, 0,
                QTableWidgetItem(task.name)
            )

            self.table.setItem(
                row, 1,
                QTableWidgetItem(task.deadline.toString("yyyy-MM-dd"))
            )

            self.table.setItem(
                row, 2,
                QTableWidgetItem(task.priority)
            )

            self.table.setItem(
                row, 3,
                QTableWidgetItem(
                    str(task.progress) + "%"
                )
            )

    def open_progress(self):

        row = self.table.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Error",
                "Select a task first."
            )

            return

        from windows.progress_window import ProgressWindow

        self.window = ProgressWindow(tasks[row])

        self.window.show()

        self.close()

    def go_back(self):

        from windows.dashboard import MainWindow

        self.window = MainWindow()
        self.window.show()
        self.close()