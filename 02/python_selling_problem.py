#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Example for the burrito selling problem"""


def nth_lowest_selling(sales, nth_val):
    """Reveive and count the ocurrences in a list,
    and get that which corresponds to the argument passed"""
    # d = {}
    # for value in set(sales):
    #     d[value] = sales.count(value)
    # for key, value in d.items():
    #     if value == n:
    #         return key
    #
    # another solution
    for value in set(sales):
        if sales.count(value) == nth_val:
            return value
    return None
