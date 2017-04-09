#!/usr/bin/env python3

"""Module containing helper methods"""

class Utility:
    """Class containing helper methods."""
    @staticmethod
    def str_to_bool(s):
        """Convert string to boolean value.

        Arguments:
            s : String to convert.

        Returns:
            True or False.
        """
        if s == 'False':
            return False
        else:
            return True


