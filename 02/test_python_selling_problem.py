#!/usr/bin/env python

"""Tests for `python_selling_problem` package."""

from python_selling_problem import nth_lowest_selling as nthls


def test_check_the_n_sale():
    """With n=2 check if the id=2 in the sales is the
    n-th position in quantity of sales."""
    sales = [5, 4, 3, 2, 1,
             5, 4, 3, 2,
             5, 4, 3,
             5, 4,
             5]
    res0 = nthls(sales, 2)
    res1 = nthls(sales, 5)
    assert res0 == 2 and res1 == 5


def test_check_the_nth_sale_with_characters():
    """Whith a list of sales based on different types
    find the n-th element corresponding type (character)"""
    sales = ['a', 'b', 'c', 'd', 'e',
             'a', 'b', 'c', 'd',
             'a', 'b', 'c',
             'a', 'b',
             'a']
    res0 = nthls(sales, 1)  # Waits for 'e'
    res1 = nthls(sales, 5)  # Waits for 'a'
    assert res0 == 'e' and res1 == 'a'
