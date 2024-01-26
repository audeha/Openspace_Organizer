import os
from src.utils import hello
from src.table import Table
from src.openspace import OpenSpace

"""here we set the output_file index to 1 so that it creates a new file each time the script runs"""
def find_next_available_filename(base_path, extension):
    index = 1
    while True:
        filename = f"{base_path}{index}.{extension}"
        if not os.path.exists(filename):
            return filename
        index += 1

def main():
    # Get the list of people from the hello function
    people = hello()

    # Create tables
    tables = [Table(table_capacity) for _ in range(number_of_tables)]

    # Create an OpenSpace instance with the tables
    open_space = OpenSpace(tables, number_of_tables)

    # Organize people in OpenSpace
    open_space.organize(people)

    # Display the seating arrangement
    open_space.display()

    # Find the next available filename
    filename = find_next_available_filename('org_colleagues', 'txt')

    # Store the seating arrangement in the new file
    open_space.store(filename)
    print(f"org saved in {filename}")

if __name__ == "__main__":
    main()
