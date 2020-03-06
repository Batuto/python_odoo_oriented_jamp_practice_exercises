#!/usr/bin/env python

"""Tests for `python_sum_list_problem` package."""


import python_sum_list_problem as pslp


def test_add_three_numbers_and_check_for_inexistent_result():
    """Add the 3 initial numbers and then check for the
    first result and an inexistent result."""
    data_s = pslp.MovingTotal()
    data_s.append([1, 2, 3])
    rest = data_s.contains(6)
    resf = data_s.contains(7)
    assert rest and not resf


def test_add_one_number_after_three_initial_numbers():
    """Add one number after the three initial numbers,
    then check  for the existence of the first and second
    results."""
    data_s = pslp.MovingTotal()
    data_s.append([1, 2, 3])
    data_s.append([4])
    res0 = data_s.contains(6)
    res1 = data_s.contains(9)
    assert res0 and res1
