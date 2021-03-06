# -*- coding: utf-8 -*-

"""
pyaction.datetime_.objects
~~~~~~~~~~~~~~~~~~~~~~~~~~

The main objects of the datetime field.

"""

__all__ = ['create_dates_list', 'time_until_end_of_day']

import datetime

#-----------------------------------------------------------------------------

def create_dates_list(start_date, end_date, input_format="%m/%d/%Y", output_format="%m/%d/%Y"):
    """
    Creates a list of dates within the specified range.

    Args:
        start_date (str): The start date. Included in the output list.
        end_date (str): The end date. Also included in the ouput list.
        input_format (str): Format of the `start_date` and `end_date`.
            Defaults to "%m/%d/%Y".
        output_format (str): Format of the dates in the ouptut list.
            Defaults to "%m/%d/%Y".

    Returns:
        :obj:`list` of :obj:`str`: The list with dates.

    """

    sdate = datetime.datetime.strptime(start_date, input_format)
    edate = datetime.datetime.strptime(end_date, input_format)
    date_list = [(edate - datetime.timedelta(days=x)).strftime(output_format) for x in range((edate - sdate).days + 1)]

    return list(reversed(date_list))

def time_until_end_of_day():
    """
    Finds the time before the end of the day.

    Returns:
        int: Time before the end of the day in seconds.
        
    """

    dt = datetime.datetime.now()
    tomorrow = dt + datetime.timedelta(days=1)
    rest_time = (datetime.datetime.combine(tomorrow, datetime.time.min) - dt).total_seconds()

    return int(rest_time)

#-----------------------------------------------------------------------------
