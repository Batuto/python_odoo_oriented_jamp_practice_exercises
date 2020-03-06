#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This data structure that can, efficiently store and
check if the total of any three successively added elements
"""


class MovingTotal:
    """Data structure to store and sum elements"""
    def __init__(self):
        self.list = []
        self.results = []

    def append(self, int_list):
        """This method evaluates the input and appends or extends
        the content"""
        if len(self.list) < 3:
            if len(int_list) == 3:
                self.list.extend(int_list)
                self.results.append(sum(int_list))
            else:
                raise Exception(ValueError,
                                'You must provide a list with 3 integers.')

        else:
            if len(int_list) == 1:
                self.list.extend(int_list)
                self.results.append(sum(self.list[-3:]))
            else:
                raise Exception(ValueError,
                                'This usage case is not yet implemented.')

    def contains(self, value):
        """This method check the existence of a value"""
        # return True if self.results.count(value) != 0 else False
        return bool(self.results.count(value))
