class Seat:
    def __init__(self):
        """ initializes the seat as free and without an occupant"""
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        """ allows the program to assign someone a seat if it's free """
        if self.free:
            self.occupant = name
            self.free = False
            #print(f"Seat assigned to {name}")
        else:
            print("Seat is taken")

    def remove_occupant(self):
        """removes someone from a seat and returns the name of the person
        occupying the seat before"""
        if not self.free:
            removed_occupant = self.occupant
            self.occupant = None
            self.free = True
            print(f"Removed: {removed_occupant}")
            return removed_occupant
        else:
            print("Seat is already free")
            #returns None because the seat was free
            return None


class Table:
    def __init__(self, capacity=24):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    """Checks if there is at least one free seat at the table"""
    def has_free_spot(self):
        """any(iterable): Return True if any element of the iterable is true.
        If the iterable is empty, return False"""
        return any(seat.free for seat in self.seats)

    """Give a seat to someone"""
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return f"{name} is seated."
        return "No free seats available."

    """Returns a number of free seats at the table"""
    def capacity_left(self):
        return sum(seat.free for seat in self.seats)
