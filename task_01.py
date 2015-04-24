#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Function for exception.
        Args:
            var1:input value for function
            var2:input value for function
        Returns:
            returns an error message if invalid key or index is accessed.
        Examples:
            >>> simple_lookup([1,2], 4)
            Warning: Your index/key doesn't exist
            >>> simple_lookup({}, 'banana')
            Warning: Your index/key doesn't exist.
    """
    try:
        return var1[var2]
    except (KeyError, IndexError):
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
