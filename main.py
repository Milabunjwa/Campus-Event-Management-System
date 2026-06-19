from event_manager import EventManager

manager = EventManager()

while True:

    print("\n===== Campus Event Management =====")
    print("1. Add Student")
    print("2. Create Event")
    print("3. Register Student")
    print("4. View Events")
    print("5. View Registrations")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Student Name: ")

        manager.add_student(
            student_id,
            name
        )

        print("Student added.")

    elif choice == "2":

        event_id = input("Event ID: ")
        title = input("Event Title: ")
        date = input("Event Date: ")

        manager.create_event(
            event_id,
            title,
            date
        )

        print("Event created.")

    elif choice == "3":

        student_id = input("Student ID: ")
        event_id = input("Event ID: ")

        manager.register_student(
            student_id,
            event_id
        )

        print("Registration successful.")

    elif choice == "4":

        for event in manager.get_events():
            print(event)

    elif choice == "5":

        for registration in manager.get_registrations():
            print(registration)

    elif choice == "6":
        break

    else:
        print("Invalid option.")