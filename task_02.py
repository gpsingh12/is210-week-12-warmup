#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """ Exception is parent class for InvalidAgeError.
        Check invalid age and raise an error
    Attributes:
        None
    """
    pass


def get_age(birthyear):
    """Function convert birth year to age.
    Args:
        birthyear(int): input value of birthyear to be converted.
    Returns:
        returns age, if birthyear is valid, otherwise return error.
    Examples:
        >>> get_age(2099)
        Traceback (most recent call last):
            File "<stdin>"' line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
