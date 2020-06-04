"""
The previous tasks have been logging messages through helper functions provided in the logging library and
using the root Logger.

Typically you will get local Logger objects for each module and call logging functions on that object.
This is done by calling "logging.getLogger()" which returns a Logger object for a given name.
You should never directly create instances of a Logger object.

Calling "logging.getLogger()" with no arguments, will return the root Logger.

In this task, we have created a module scoped "logger" instance with the name "mortgage".
Replace the logging calls with references to this instance.

After you execute this code, you should notice the name "mortgage" is now included in the output.
"""
from __future__ import print_function
import math
import logging

logger = logging.getLogger('mortgage')


def get_current_rate(years):
    logger.debug('Fetching current interest rate for %d years' % years)
    rate = 5.3  # Stub external service call
    logger.debug('Service returned interest rate %f' % rate)
    return rate


def get_monthly_payment(principal, years):
    logger.info('Calling mortgage calculator')

    if years > 50:
        logger.warning('Term greater than 50 years')

    mon_rate = get_current_rate(years) / 1200
    payments = years * 12
    logger.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate / (1 - math.pow((1 + mon_rate), -payments)))

    logger.debug('Calculated result is %f' % result)
    logger.debug('Leaving mortgage calculator')
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
