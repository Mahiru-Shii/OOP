from PyQt5.QtWidgets import *


class ProgressWindow(QWidget):

    def __init__(self, task):
        super().__init__()

        self.task = task

        self.setWindowTitle("Update Progress")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout()

        title = QLabel(task.name)

        self.progress = QSpinBox()
        self.progress.setRange(0, 100)
        self.progress.setValue(task.progress)

        save_btn = QPushButton("Save")

        save_btn.clicked.connect(
            self.save_progress
        )

        layout.addWidget(title)
        layout.addWidget(self.progress)
        layout.addWidget(save_btn)

        self.setLayout(layout)

    def save_progress(self):

        self.task.update_progress(
            self.progress.value()
        )

        QMessageBox.information(
            self,
            "Success",
            "Progress Updated"
        )

        from windows.task_list import TaskListWindow

        self.window = TaskListWindow()

        self.window.show()

        self.close()