import random

class OpenSpace:
    """numbers_of_tables is an integer representing the number of tables)
    and tables is a list of Table objects)"""
    def __init__(self, tables, numbers_of_tables):
        if len(tables) != numbers_of_tables:
            raise ValueError("The number of tables provided does not match the expected count.")
        self.tables = tables

    """Randomly assign people to the Seat objects in the different Table objects"""
    def organize(self, names):
        #copy new table list
        shuffled_tables = self.tables[:]
        """Return a k length list of unique elements chosen from the set.
          Used for random sampling without replacement.
          random.sample(set, k)"""
        shuffled_names = random.sample(names, len(names))
        for name in shuffled_names:
            #shuffle the order of the table
            random.shuffle(shuffled_tables)
            for table in shuffled_tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    """Display the different tables and their occupants in a nice and readable way"""
    def display(self):
        """iterating over each Table object in the self.tables list
        while keeping track of the index of each table."""
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}:")
            for seat in table.seats:
                if seat.occupant:
                    occupant = seat.occupant
                else:
                    occupant = "Empty"
                print(f" * {occupant}")
            free_seats = table.capacity_left()
            print(f"Table {i+1} has {free_seats} free seats left.")
            print()  # New line for better readability

    """Store the repartition in org_colleagues.txt"""
    def store(self, filename):
        with open(filename, 'w') as file:
            for i, table in enumerate(self.tables):
                file.write(f"Table {i + 1}:\n")
                for seat in table.seats:
                    occupant = seat.occupant if seat.occupant else "Empty"
                    file.write(f" - {occupant}\n")
                file.write("\n")
