class Event:

    def __init__(self, event_id, title, date):
        self.event_id = event_id
        self.title = title
        self.date = date

    def __str__(self):
        return f"{self.event_id} | {self.title} | {self.date}"