from the_shortest_person_in_the_room import Person
class Room:
    list_of_rooms = []
    def add(self, person: Person):
        self.list_of_rooms.append(person)

    def is_empty(self):
        return len(self.list_of_rooms) == 0

    def print_contents(self):
        for rooms in self.list_of_rooms:
            print(f"{rooms.name} ({rooms.height} cm)")
        # return f"there are {len(self.list_of_rooms)} persons in the room, and their combined height is "

    def find_shortest(self):
        shortest_person = Person("tallest", 18999)
        for person in self.list_of_rooms:
            if person.height < shortest_person.height:
                shortest_person = person

        if len(self.list_of_rooms) == 0:
            return None
        else:
            return shortest_person

    def shortest(self):
        shortest_person = self.find_shortest()
        return shortest_person.name

    def remove_shortest(self):
        shortest_person = self.find_shortest()
        self.list_of_rooms.remove(shortest_person)
        return shortest_person.name
  





room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed}")

print()

room.print_contents()

lea = Person("Lea", 183)

lea_str = "Lea"