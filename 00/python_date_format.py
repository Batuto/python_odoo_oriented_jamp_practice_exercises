#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example to return a list of formatted dates
"""

import logging
from datetime import datetime as dt


def fun(date, dformat):
    """This function receives a date with certain format and tries to
    transform it to a new format"""
    try:
        parsed = dt.strftime(dt.strptime(date, dformat), '%Y%m%d')
        return [parsed]
    except ValueError as val_error:
        logging.warning(val_error)
        return []


def change_date_format(date_list):
    """This function receive a list with strings representing dates
    and return another list with the dates formatted"""
    if not isinstance(date_list, list):
        return None
    result = []
    for val in date_list:
        # for format in ['%Y/%m/%d', '%d/%m/%Y', '%m-%d-%Y']:
        for date_format in ['%Y/%m/%d', '%d/%m/%Y', '%m-%d-%Y']:
            result.extend(fun(val, date_format))
        # if 4 == val.find('/'):
        #    result.append(fun(val, '%Y/%m/%d'))
        # if 2 == val.find('/'):
        #    result.append(fun(val, '%d/%m/%Y'))
        # if 2 == val.find('-'):
        #    result.append(fun(val, '%m-%d-%Y'))
    return result
