#!/usr/bin/env python3

"""
Brief description.
"""

class SubClass:
    """
    This is a sample class

    Attributes:
        month (str): Month
    Methods:
        print_month(): Prints the month
    """
    def __init__(self, month):
        """
        Constructs all the necessary attributes for the class

        Args:
            month (str): Month
        """
        self.month = month

    def print_month(self):
        """
        This function prints the month
        """
        print("The month is " + self.month)
