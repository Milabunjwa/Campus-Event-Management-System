from event_manager import EventManager

manager = EventManager()

while True:

    print("\n===== Campus Event Management =====")
    print("1. Add Student")
    print("2. Create Event")
    print("3. Register Student")
    print("4. View Events")
    print("5. View Registrations")
    print("6. Search Event by ID")
    print("7. Search Event by Title")
    print("8. Search Student by ID")
    print("9. Search Student by Name")
    print("10. Exit")

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

        capacity = int(input("Capacity: "))

        manager.create_event(
        event_id,
        title,
        date,
        capacity
    )
        print("Event created.")

    elif choice == "3":

        student_id = input("Student ID: ")
        event_id = input("Event ID: ")

        success = manager.register_student(
            student_id,
            event_id
        )
        if success:
            print(
            "Registration successful."
        )
        else:
            print(
        "Registration failed."
        )

    elif choice == "4":

        for event in manager.get_events():
            print(event)

    elif choice == "5":

        for registration in manager.get_registrations():
            print(registration)

    elif choice == "6":

        event_id = input("Enter Event ID: ")
        event = manager.find_event_by_id(event_id)
        if event:
            print(event)
        else:
            print("Event not found.")

    elif choice == "7":

        title = input(
            "Enter Event Title: "
        )
        results = manager.find_event_by_title(
            title
        )
        if results:

            for event in results:
                print(event)
        else:
            print("No matching events found.")

    elif choice == "8":

        student_id = input(
            "Enter Student ID: "
        )

        student = manager.find_student_by_id(
            student_id
        )

        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "9":

        name = input(
            "Enter Student Name: "
        )

        results = manager.find_student_by_name(
            name
        )

        if results:

            for student in results:
                print(student)

        else:
            print("No students found.")

    elif choice == "10":
        break