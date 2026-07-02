class Event:

    def __init__(
            self,
            event_id,
            title,
            date,
            capacity
    ):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.capacity = capacity

    def __str__(self):
        return (
            f"{self.event_id} | "
            f"{self.title} | "
            f"{self.date} | "
            f"Capacity: {self.capacity}"
        )