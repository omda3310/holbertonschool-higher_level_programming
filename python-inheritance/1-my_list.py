#!/usr/bin/python3
class Mylist(list):
    """Mylist class"""

    def print_sorted(self):
        """Print sorted list"""
        list_out = list.copy(self)
        list.sort(list_out)
        print(list_out)
