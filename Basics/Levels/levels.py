"""
The logging module provides five logging levels.
The levels allow you to control what messages are included in the output stream.
Five levels is usually good for most applications,
as having more levels just leads to confusion about which level to use.

Each level is known by a constant (in all caps) and has a numeric value.
The value comes into play when setting a log level on a logger.
Only messages at the logger's current logging level or greater is output.

LEVEL NAME         | FUNCTION                | VALUE
===================+=========================+==========
CRITICAL           | critical()              | 50
ERROR              | error()                 | 40
WARNING            | warning() or warn()     | 30
INFO               | info()                  | 20
DEBUG              | debug()                 | 10

(1) Change the "Calling mortgage calculator" call to log with an INFO level.

(2) Then log a WARNING level message when the years is greater than 50.
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
    logging.info('Calling mortgage calculator')

    if years > 50:
        logging.warning('years > 50 ')

    mon_rate = get_current_rate(years) / 1200
    payments = years * 12
    logging.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate / (1 - math.pow((1 + mon_rate), -payments)))

    logging.debug('Calculated result is %f' % result)
    logging.debug('Leaving mortgage calculator')
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 300)
    print('Monthly payment is %f' % payment)
