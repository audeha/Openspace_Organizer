from src.table import Table, Seat
from src.utils import hello

def main():
    #get the list of people from the hello function
    people = hello()

    # create a table instance
    table1 = Table()

    # Assign people to the table
    for person in people:
        if table1.has_free_spot():
            assignment_message = table1.assign_seat(person)
            print(assignment_message)
        else:
            print("No free spots available at the table.")

    # Check table status
    print("Are there free spots at the table?", table1.has_free_spot())
    print("Capacity left at the table:", table1.capacity_left())

    # Create a Seat instance for each person
    seats = [Seat() for _ in range(len(people))]

    # Assign each person to a seat
    for person, seat in zip(people, seats):
        seat.set_occupant(person)

    # Example: Remove the first person from their seat and print the result
    removed_name = seats[0].remove_occupant()
    print(f"Seat is now free, removed occupant was: {removed_name}")

    # Print the status of each seat
    for i, seat in enumerate(seats):
        occupant = seat.occupant if seat.occupant else "Empty"
        print(f"Seat {i + 1}: {occupant}")


if __name__ == "__main__":
    main()
