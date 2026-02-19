"""
CS 562 - Assignment 1: Kids Running in the Yard
Author: Kellie Clark
Date: 2026-02-09
"""

from PersonFactory import PersonFactory

class FamilyTree:
    """Driver class that builds and stores a family tree as well as provides methods for querying the data."""
    def __init__(self):
        """Initializes FamilyTree with an PeopleFactory instance and an empty people list to store the total people in the tree."""
        self.person_factory = PersonFactory()
        self.person_factory.read_files()
        self.people = []

    def generate_tree(self):
        """Generates a tree by calling the PersonFactory.py to generate people object that start with a birth year of 1950 and end with the birth year 2120"""
        person_one = self.person_factory.get_person("1950")
        person_two = self.person_factory.get_person("1950")

        # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
        self.people.append(person_one)
        if person_one.get_partner() is not None:
            self.people.append(person_one.get_partner())
        for child in person_one.get_children():
            self.people.append(child)

        # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
        self.people.append(person_two)
        if person_two.get_partner() is not None:
            self.people.append(person_two.get_partner())
        for child in person_two.get_children():
            self.people.append(child)

        curr_gen = []
        for child in person_one.get_children():
            curr_gen.append(child)
        for child in person_two.get_children():
            curr_gen.append(child)

        while curr_gen != []:
            next_gen = []
            for person in curr_gen:
                # Source: Python docs - int() for type conversion to integer - https://docs.python.org/3/library/functions.html#int
                year_born = int(person.get_year_born())
                if year_born <= 2120:
                    partner = self.person_factory.generate_partner(person.get_year_born())

                    # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
                    if partner is not None:
                        person.set_partner(partner)
                        self.people.append(partner)

                    children = self.person_factory.generate_children(person.get_year_born(), person.get_partner(), person.get_last_name())
                    if children != 0:
                        for child in children:
                            person.add_child(child)
                            next_gen.append(child)
                            self.people.append(child)

                            # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
                            if partner is not None:
                                partner.add_child(child)

            curr_gen = next_gen

    def total_people(self):
        """Counts the total number of people in a family tree."""
        num_people = len(self.people)
        print("The tree contains " + str(num_people) + " people total")

    def people_by_decade(self):
        """Sorts the people in the people list and creates a dictionary that maps a decade to the number of people born in that decade."""
        self.by_decade = {}
        for person in self.people:
            year = person.get_year_born()
            decade = str(year)[:3]
            decade = decade + "0"

            # Source: Pattern from Claude (LLM) — build list in dictionary by checking if key exists
            if decade not in self.by_decade:
                self.by_decade[decade] = 0
            self.by_decade[decade] = self.by_decade[decade] + 1

        for decade in self.by_decade:
            print(decade + ": " + str(self.by_decade[decade]))

    def duplicate_names(self):
        """Reads through people list to determine if there are any duplicate people with the same first and last name."""
        self.find_duplicates = {}
        for person in self.people:
            first_name = person.get_first_name()
            last_name = person.get_last_name()
            full_name = first_name + " " + last_name

            # Source: Pattern from Claude (LLM) — build list in dictionary by checking if key exists
            if full_name not in self.find_duplicates:
                self.find_duplicates[full_name] = 0
            self.find_duplicates[full_name] = self.find_duplicates[full_name] + 1

        dupe_count = 0
        for full_name in self.find_duplicates:
            if self.find_duplicates[full_name] > 1:
                dupe_count = dupe_count + 1

        if dupe_count == 1:
            print("There is " + str(dupe_count) + " duplicate name in the tree:")
        else:
            print("There are " + str(dupe_count) + " duplicate names in the tree:")

        for full_name in self.find_duplicates:
            if self.find_duplicates[full_name] > 1:
                print("* " + full_name)

    def user_interaction(self):
        """Allows a user to interact with the FamilyTree by offering a menu and taking their input."""
        print("Are you interested in:")
        print("(T)otal number of people in the tree")
        print("Total number of people in the tree by (D)ecade")
        print("(N)ames duplicated")
        print("(Q)uit")
        print()

        # Source: Python docs - input() for reading user input - https://docs.python.org/3/library/functions.html#input
        choice = input("Enter choice: ")
        print()

        # Source: Python docs - str.upper() for converting string to uppercase - https://docs.python.org/3/library/stdtypes.html#str.upper
        choice = choice.upper()

        while choice != "Q":
            if choice == "T":
                self.total_people()
            elif choice == "D":
                self.people_by_decade()
            elif choice == "N":
                self.duplicate_names()
            else:
                print("Invalid choice, please try again.")
            print()
            print("Are you interested in:")
            print("(T)otal number of people in the tree")
            print("Total number of people in the tree by (D)ecade")
            print("(N)ames duplicated")
            print("(Q)uit")
            print()


            # Source: Python docs - input() for reading user input - https://docs.python.org/3/library/functions.html#input
            choice = input("Enter choice: ")
            print()

            # Source: Python docs - str.upper() for converting string to uppercase - https://docs.python.org/3/library/stdtypes.html#str.upper
            choice = choice.upper()


        print("Goodbye!")

# Print menu so user can interact
print("Reading files...")
tree = FamilyTree()
print("Generating family tree...")
tree.generate_tree()
tree.user_interaction()
