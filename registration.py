class Registration:

    def __init__(self, student, event):
        self.student = student
        self.event = event

    def __str__(self):
        return f"{self.student.name} registered for {self.event.title}"