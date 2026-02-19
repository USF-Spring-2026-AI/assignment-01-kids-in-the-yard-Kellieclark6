"""
CS 562 - Assignment 1: Kids Running in the Yard
Author: Kellie Clark
Date: 2026-02-09
"""

class Person:
    """Stores a single person's data."""

    def __init__(self, year_born, year_died, first_name, last_name, gender):
        """Constructor for person object that initializes attributes."""
        self.year_born = year_born
        self.year_died = year_died
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.partner = None
        self.children = []

    def get_year_born(self):
        return self.year_born

    def get_year_died(self):
        return self.year_died

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_gender(self):
        return self.gender

    def get_partner(self):
        return self.partner

    def get_children(self):
        return self.children

    def set_partner(self, partner):
        self.partner = partner

    def set_children(self, children):
        self.children = children

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        """Return a string with the person's details."""
        return ('Name: ' + self.first_name + ' ' + self.last_name + '\nGender: ' + self.gender +
                '\nLived: ' + str(self.year_born) + ' - ' + str(self.year_died) + '\nPartner/ Spouse: ' +
                str(self.partner) + '\nChildren: ' + str(self.children))
