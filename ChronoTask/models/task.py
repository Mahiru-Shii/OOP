class Task:

    def __init__(self, name, description, deadline, priority):
        self.name = name
        self.description = description
        self.deadline = deadline   # QDate object
        self.priority = priority
        self.progress = 0

    def update_progress(self, value):
        self.progress = value