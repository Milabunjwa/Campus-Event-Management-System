from student import Student
from event import Event
from registration import Registration


class EventManager:

    def __init__(self):
        self.events = []
        self.students = []
        self.registrations = []

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def create_event(self, event_id, title, date):
        event = Event(event_id, title, date)
        self.events.append(event)

    def register_student(self, student_id, event_id):

        student = None
        event = None

        for s in self.students:
            if s.student_id == student_id:
                student = s

        for e in self.events:
            if e.event_id == event_id:
                event = e

        if student and event:
            registration = Registration(student, event)
            self.registrations.append(registration)

    def get_events(self):
        return self.events

    def get_registrations(self):
        return self.registrations

    def find_event_by_id(self, event_id):

        for event in self.events:
            if event.event_id == event_id:
                return event

        return None

    def find_event_by_title(self, title):

        matches = []

        for event in self.events:
            if title.lower() in event.title.lower():
                matches.append(event)

        return matches