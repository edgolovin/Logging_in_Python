"""
The following code is typical of how many people start debugging their programs using the "print" function.

The problem with using "print" to output debugging information, is it does not work well in larger programs.
The debug output interferes with application output and you typically end up commenting out or
removing all this extra code when you are not debugging.

The standard logging module provides an easy way to separate application output from debug output.

In this task, replace the highlighted "print" function calls with calls to "logging.debug".
"""
from __future__ import print_function
import math
import logging


def get_current_rate(years):
    logging.debug('Fetching current interest rate for %d years' % years)
    rate = 7.5  # Stub external service call
    logging.debug('Service returned interest rate %f' % rate)
    return rate


def get_monthly_payment(principal, years):
    logging.debug('Calling mortgage calculator')

    mon_rate = get_current_rate(years) / 1200
    payments = years * 12
    logging.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate / (1 - math.pow((1 + mon_rate), -payments)))

    logging.debug('Calculated result is %f' % result)
    logging.debug('Leaving mortgage calculator')
    return result


if __name__ == '__main__':
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
