#!/usr/bin/env python

"""Tests for `python_date_format` package."""


from python_date_format import change_date_format


def test_format_3_valid_strings():
    """Format 3 valid strings"""
    res = change_date_format(["2013/08/21", "18/12/2020",
                              "12-04-2009", "20130720"])
    assert res == ["20130821", "20201218", "20091204"]


def test_format_1_invalid_string():
    """Format 1 valid string"""
    res = change_date_format(["20130720"])
    assert res == []


def test_format_3_invalid_strings():
    """Format 3 invalid strings"""
    res = change_date_format(["2013/98/21", "i8d12a2020",
                              "00-84-0000", "20130720"])
    assert res == []
