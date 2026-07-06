import os
import unittest
from event_manager import EventManager


class TestEventManager(unittest.TestCase):

    def setUp(self):
        self.manager = EventManager()

    def test_add_student(self):
        self.manager.add_student("S001", "Mila")

        self.assertEqual(
            len(self.manager.students),
            1
        )

    def test_create_event(self):
        self.manager.create_event(
            "E001",
            "Career Fair",
            "2026-07-15",
            100
        )

        self.assertEqual(
            len(self.manager.events),
            1
        )

    def test_register_student(self):
        self.manager.add_student(
            "S001",
            "Mila"
        )

        self.manager.create_event(
        "E001",
        "Career Fair",
        "2026-07-15",
        100
    )

        self.manager.register_student(
            "S001",
            "E001"
        )

        self.assertEqual(
            len(self.manager.registrations),
            1
        )

    def test_get_events(self):
        self.manager.create_event(
            "E001",
            "Career Fair",
            "2026-07-15",
            100
        )

        self.assertEqual(
            len(self.manager.get_events()),
            1
        )

    def test_get_registrations(self):
        self.manager.add_student(
            "S001",
            "Mila"
        )

        self.manager.create_event(
        "E001",
        "Career Fair",
        "2026-07-15",
        100
    )

        self.manager.register_student(
            "S001",
            "E001"
        )

        self.assertEqual(
            len(self.manager.get_registrations()),
            1
        )

    def test_find_event_by_id(self):

        self.manager.create_event(
        "E001",
        "Career Fair",
        "2026-07-15",
        100
    )

        event = self.manager.find_event_by_id(
            "E001"
        )

        self.assertIsNotNone(event)

    def test_find_event_by_title(self):

        self.manager.create_event(
        "E001",
        "Career Fair",
        "2026-07-15",
        100
    )

        results = self.manager.find_event_by_title(
            "Career"
        )

        self.assertEqual(
            len(results),
            1
        )

    def test_find_student_by_id(self):

        self.manager.add_student(
            "S001",
            "Mila"
        )

        student = self.manager.find_student_by_id(
            "S001"
        )

        self.assertIsNotNone(student)

    def test_find_student_by_name(self):

        self.manager.add_student(
            "S001",
            "Mila"
        )

        results = self.manager.find_student_by_name(
            "Mil"
        )

        self.assertEqual(
            len(results),
            1
        )

    def test_event_capacity_limit(self):

        self.manager.add_student(
            "S001",
            "Mila"
        )

        self.manager.add_student(
            "S002",
            "John"
        )

        self.manager.create_event(
            "E001",
            "Career Fair",
            "2026-07-15",
            1
        )

        self.assertTrue(
            self.manager.register_student(
                "S001",
                "E001"
            )
        )

        self.assertFalse(
            self.manager.register_student(
                "S002",
                "E001"
            )
        )

    def test_save_events(self):

        self.manager.create_event(
            "E001",
            "Career Fair",
            "2026-07-15",
            100
        )

        self.manager.save_events()

        self.assertTrue(
            os.path.exists(
                "data/events.json"
            )
        )


if __name__ == "__main__":
    unittest.main()