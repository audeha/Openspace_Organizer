import argparse
import json
from src.utils import hello
from src.table import Table
from src.openspace import OpenSpace

def main(name_path):
    # Read config.json file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Use the configuration variables
    number_of_tables = config['number_of_tables']
    table_capacity = config['table_capacity']

    # Get the list of people from the hello function
    people = hello(name_path)
    print("There are ", len(people), "people that wait to be seated.")

    # Create tables
    tables = [Table(table_capacity) for _ in range(number_of_tables)]

    # Create an OpenSpace instance with the tables
    open_space = OpenSpace(tables, number_of_tables)

    # Organize people in OpenSpace
    open_space.organize(people)

    # Display the seating arrangement
    open_space.display()

    # Store the seating arrangement in file
    open_space.store('org_colleagues.txt')

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process the path of the input file.")

    # Add an argument for the input file path
    parser.add_argument('input_file_path', type=str, help='Path to the input file')

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the input file path
    main(args.input_file_path)
