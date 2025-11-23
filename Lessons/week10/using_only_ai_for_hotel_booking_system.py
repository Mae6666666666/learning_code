

rooms = {
    101: {"type": "Single", "price": 80, "booked": False},
    102: {"type": "Single", "price": 80, "booked": False},
    201: {"type": "Double", "price": 120, "booked": False},
    202: {"type": "Double", "price": 120, "booked": False},
    301: {"type": "Suite", "price": 250, "booked": False},
}

bookings = {}

def show_rooms():
    print("\n--- Available Rooms ---")
    for room, info in rooms.items():
        status = "Booked" if info["booked"] else "Available"
        print(f"Room {room}: {info['type']} - ${info['price']} ({status})")


def book_room():
    show_rooms()
    try:
        room_number = int(input("\nEnter the room number to book: "))
        if room_number not in rooms:
            print("Invalid room number.")
        elif rooms[room_number]["booked"]:
            print("Sorry, that room is already booked.")
        else:
            name = input("Enter your name: ")
            rooms[room_number]["booked"] = True
            bookings[room_number] = name
            print(f"Room {room_number} successfully booked for {name}!")
    except ValueError:
        print("Please enter a valid number.")


def cancel_booking():
    try:
        room_number = int(input("\nEnter room number to cancel booking: "))
        if room_number in bookings:
            print(f"Booking for {bookings[room_number]} has been canceled.")
            rooms[room_number]["booked"] = False
            del bookings[room_number]
        else:
            print("No booking found for that room.")
    except ValueError:
        print("Invalid room number.")


def show_bookings():
    print("\n--- Current Bookings ---")
    if not bookings:
        print("No rooms are currently booked.")
    else:
        for room, name in bookings.items():
            print(f"Room {room}: booked by {name}")


def menu():
    while True:
        print("\n=== Hotel Booking System ===")
        print("1. View rooms")
        print("2. Book a room")
        print("3. Cancel a booking")
        print("4. View all bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            show_bookings()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()