from PyQt5.QtWidgets import *


class ConfirmationWindow(QWidget):
    def __init__(self, task):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            f"""
Task Saved!

Task: {task.name}
Deadline: {task.deadline}
Priority: {task.priority}
"""
        )

        layout.addWidget(label)

        self.setLayout(layout)