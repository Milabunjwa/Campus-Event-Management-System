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
            "2026-07-15"
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
            "2026-07-15"
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
            "2026-07-15"
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
            "2026-07-15"
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
            "2026-07-15"
        )

        event = self.manager.find_event_by_id(
            "E001"
        )

        self.assertIsNotNone(event)

    def test_find_event_by_title(self):

        self.manager.create_event(
            "E001",
            "Career Fair",
            "2026-07-15"
        )

        results = self.manager.find_event_by_title(
            "Career"
        )

        self.assertEqual(
            len(results),
            1
        )


if __name__ == "__main__":
    unittest.main()