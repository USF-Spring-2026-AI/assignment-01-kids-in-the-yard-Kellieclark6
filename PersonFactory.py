"""
CS 562 - Assignment 1: Kids Running in the Yard
Author: Kellie Clark
Date: 2026-02-09
"""
import random
from Person import Person
import math

class PersonFactory:
    """Reads csv files and generates Person objects with random attributes based on statistics."""

    def __init__(self):
        """Initializes PersonFactory with empty data attributes."""
        self.birth_marriage_rates = None
        self.first_names = None
        self.gender_name_prob = None
        self.last_names = None
        self.life_expect = None
        self.rank_prob = None

    def read_files(self):
        """Reads CSV files and stores data in dictionaries."""
        with open("birth_and_marriage_rates.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.birth_marriage_rates = {}
            for row in lines[1:]:
                decade = row[0]
                self.birth_marriage_rates[decade] = [row[1], row[2]]


        with open("first_names.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.first_names = {}
            for row in lines[1:]:
                key = row[0] + '_' + row[1]

                # Source: Pattern from Claude (LLM) — build list in dictionary by checking if key exists
                if key not in self.first_names:
                    self.first_names[key] = []
                self.first_names[key].append([row[2], row[3]])

        with open("gender_name_probability.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.gender_name_prob = {}
            for row in lines[1:]:
                key = row[0] + '_' + row[1]
                self.gender_name_prob[key] = row[2]


        with open("last_names.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.last_names = {}
            for row in lines[1:]:
                key = row[0] + '_' + row[1]
                self.last_names[key] = row[2]

        with open("life_expectancy.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.life_expect = {}
            for row in lines[1:]:
                year = row[0]
                self.life_expect[year] = row[1]

        with open("rank_to_probability.csv") as f:

            # Source: Python docs - str.split() for splitting string by delimiter - https://docs.python.org/3/library/stdtypes.html#str.split
            lines = [line.rstrip().split(",") for line in f]
            self.rank_prob = lines[0]

    def generate_gender(self, decade):
        """Uses data from the gender_name_probability.csv file to randomly generate a person's gender."""
        key = decade + "_" + "male"

        # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
        male_prob = float(self.gender_name_prob[key])

        # Source: Python docs - random.uniform() for generating random float - https://docs.python.org/3/library/random.html#random.uniform
        rand_prob = random.uniform(0, 1)
        if rand_prob <= male_prob:
            gender = "male"
        else:
            gender = "female"
        return gender

    def generate_first_name(self, decade, gender):
        """Reads data from first_names.csv into two empty lists for names and frequencies to determine a random first name."""
        key = decade + "_" + gender
        names = []
        freq = []
        for row in self.first_names[key]:
            names.append(row[0])

            # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
            freq.append(float(row[1]))

        # Source: Python docs - random.choices() for weighted random selection - https://docs.python.org/3/library/random.html#random.choices
        first_name = random.choices(names, weights=freq, k=1)[0]
        return first_name

    def generate_death_year(self, birth_year):
        """Takes a birth year as input and references the data in the life_expectancy.csv and randomly adds or subtracts 10 to calculate the year of death."""

        # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
        life_expect = float(self.life_expect[str(birth_year)])

        # Source: Python docs - random.uniform() for generating random float - https://docs.python.org/3/library/random.html#random.uniform
        ten_add_sub = random.uniform(-10, 10)

        # Source: Python docs - round() for rounding to nearest integer - https://docs.python.org/3/library/functions.html#round
        # Source: Python docs - int() for type conversion to integer - https://docs.python.org/3/library/functions.html#int
        death_year = round(int(birth_year) + life_expect + ten_add_sub)
        return death_year

    # Source: Python docs - default argument values - https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
    def generate_last_name(self, birth_year, last_name=None): # default value for last name to determine if someone is marrying in or a descendant
        """Generates a random last name or returns inherited last name if one is passed in."""
        decade = str(birth_year)[:3]
        decade = decade + "0s"

        # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
        if last_name is None:

            # Source: Python docs - list() to convert range to list - https://docs.python.org/3/library/functions.html#func-list
            ranks = list(range(1, 31))
            r_prob = []
            for row in self.rank_prob:

                # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
                r_prob.append(float(row))

            # Source: Python docs - random.choices() for weighted random selection - https://docs.python.org/3/library/random.html#random.choices
            find_rank = random.choices(ranks, weights=r_prob, k=1)[0]
            key = decade + "_" + str(find_rank)
            last_name = self.last_names[key]
        else:
            last_name = last_name

        return last_name

    def generate_partner(self, birth_year):
        """Uses data from birth_and_marriage_rates.csv to randomly determine if a person is married. If married, creates and returns a new Person object for the partner."""
        decade = str(birth_year)[:3]
        decade = decade + "0s"

        # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
        marriage_rate = float(self.birth_marriage_rates[decade][1])

        # Source: Python docs - random.uniform() for generating random float - https://docs.python.org/3/library/random.html#random.uniform
        marriage_prob = random.uniform(0, 1)

        if marriage_prob <= marriage_rate:

            # Source: Python docs - random.uniform() for generating random float - https://docs.python.org/3/library/random.html#random.uniform
            # Source: Python docs - int() for type conversion to integer - https://docs.python.org/3/library/functions.html#int
            add_sub_years = int(random.uniform(-10, 10))
            partner_birth_year = add_sub_years + int(birth_year)
            if partner_birth_year < 1950:
                partner_birth_year = 1950
            if partner_birth_year > 2120:
                partner_birth_year = 2120
            part_decade = str(partner_birth_year)[:3]
            part_decade = part_decade + "0s"
            gender = self.generate_gender(part_decade)
            partner_person = Person(partner_birth_year,
                                    self.generate_death_year(partner_birth_year),
                                    self.generate_first_name(part_decade, gender),
                                    self.generate_last_name(partner_birth_year),
                                    gender)
            return partner_person

        else:
            return None

    def generate_children(self, birth_year, partner, last_name):
        """Generates a list of children for a person based on their birth year, partner, last name, and corresponding birth rate."""
        decade = str(birth_year)[:3]
        decade = decade + "0s"

        # Source: Python docs - int() for type conversion to integer - https://docs.python.org/3/library/functions.html#int
        birth_year = int(birth_year)

        # Source: Python docs - float() for type conversion - https://docs.python.org/3/library/functions.html#float
        birth_rate = float(self.birth_marriage_rates[decade][0])

        # Source: Python docs - math.ceil() for rounding up to nearest integer - https://docs.python.org/3/library/math.html#math.ceil
        min_birth_rate = math.ceil(birth_rate - 1.5)
        max_birth_rate = math.ceil(birth_rate + 1.5)

        # Source: Python docs - random.randint() for generating random integer in range - https://docs.python.org/3/library/random.html#random.randint
        num_children = random.randint(min_birth_rate, max_birth_rate)

        # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
        if partner is None:
            num_children = num_children - 1
            first_birth = birth_year + 25
        elif birth_year >= partner.get_year_born():
            first_birth = partner.get_year_born() + 25
        else:
            first_birth = birth_year + 25

        if num_children <= 0:
            return []

        if num_children == 1:
            birth_variation = 0
        else:
            birth_variation = 20/(num_children - 1)

        birthday = first_birth
        children = []
        for i in range(num_children):

            # Source: Python docs - break statement to exit a loop early - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements
            if birthday > 2120:
                break
            birth_decade = str(birthday)[:3]
            birth_decade = birth_decade + "0s"
            gender = self.generate_gender(birth_decade)
            child_person = Person(birthday,
                            self.generate_death_year(birthday),
                            self.generate_first_name(birth_decade, gender),
                            last_name,
                            gender)
            children.append(child_person)

            # Source: Python docs - round() for rounding to nearest integer - https://docs.python.org/3/library/functions.html#round
            birthday = round(birthday + birth_variation)
        return children

    def get_person(self, birth_year):
        """Creates a new person object by calling all the "generate" methods above and connecting them."""
        decade = str(birth_year)[:3]
        decade = decade + "0s"
        gender = self.generate_gender(decade)
        first_name = self.generate_first_name(decade, gender)
        last_name = self.generate_last_name(birth_year)
        death_year = self.generate_death_year(birth_year)
        new_person = Person(birth_year, death_year, first_name, last_name, gender)
        partner = self.generate_partner(birth_year)
        children = self.generate_children(birth_year, partner, last_name)

        # Source: Python docs - identity comparison with 'is' operator - https://docs.python.org/3/reference/expressions.html#is-not
        if partner is not None:
            new_person.set_partner(partner)

        if children:
            for child in children:
                new_person.add_child(child)
                if partner is not None:
                    partner.add_child(child)

        return new_person