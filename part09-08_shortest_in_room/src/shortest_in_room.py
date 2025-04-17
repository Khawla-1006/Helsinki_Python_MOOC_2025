# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.room = []
    
    def add(self, person: Person):
        self.room.append(person)

    def is_empty(self):
        if len(self.room) == 0 :
            return True
        else: 
            return False
    
    def print_contents(self):
        combined_height = 0
        for person in self.room:
            combined_height += person.height
        print(f"There are {len(self.room)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.room :
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.room) != 0 :
            shortest = self.room[0].height
            for person in self.room :
                if person.height <= shortest :
                    shortest = person.height
                    shortest_name = person
            return shortest_name
        else :
            return None
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person != None :
            removed = self.room.pop(self.room.index(shortest_person))
            return removed
        return None
    
if __name__ == "__main__" :
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()