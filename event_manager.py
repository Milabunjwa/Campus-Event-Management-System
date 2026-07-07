import json
import os
from student import Student
from event import Event
from registration import Registration


class EventManager:

    def __init__(self):
        self.events = []
        self.students = []
        self.registrations = []

        self.load_events()

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def create_event(
            self,
            event_id,
            title,
            date,
            capacity
    ):
        event = Event(
            event_id,
            title,
            date,
            capacity
        )

        self.events.append(event)
        self.save_events()

    def register_student(
            self,
            student_id,
            event_id
    ):

        student = self.find_student_by_id(
            student_id
        )

        event = self.find_event_by_id(
            event_id
        )

        if not student or not event:
            return False

        if (
                self.get_registration_count(
                    event_id
                )
                >= event.capacity
        ):
            return False

        registration = Registration(
            student,
            event
        )

        self.registrations.append(
            registration
        )

        return True

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

    def find_student_by_id(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def find_student_by_name(self, name):

        matches = []

        for student in self.students:
            if name.lower() in student.name.lower():
                matches.append(student)

        return matches

    def get_registration_count(
            self,
            event_id
    ):

        count = 0

        for registration in self.registrations:

            if (
                    registration.event.event_id
                    == event_id
            ):
                count += 1

        return count

    def save_events(self):

        event_data = []

        for event in self.events:

            event_data.append({
                "event_id": event.event_id,
                "title": event.title,
                "date": event.date,
                "capacity": event.capacity
            })

        with open(
                "data/events.json",
                "w"
        ) as file:

            json.dump(
                event_data,
                file,
                indent=4
            )

    def load_events(self):

        try:

            with open(
                    "data/events.json",
                    "r"
            ) as file:

                event_data = json.load(
                    file
                )
                self.events.clear()

                for event in event_data:

                    loaded_event = Event(
                        event["event_id"],
                        event["title"],
                        event["date"],
                        event["capacity"]
                    )

                    self.events.append(
                        loaded_event
                    )

        except FileNotFoundError:
            pass

    def generate_attendance_report(self):

        report = []

        for event in self.events:

            attendee_count = 0

            for registration in self.registrations:

                if (
                        registration.event.event_id
                        == event.event_id
                ):
                    attendee_count += 1

            report.append({
                "event": event.title,
                "attendees": attendee_count
            })

        return report