"""
We mentioned in a previous task, there are 5 severity levels : CRITICAL, ERROR, INFO, WARNING, DEBUG.

There are a few exceptions. First, a few of the levels have several constants defined.
FATAL can be used instead of CRITICAL. There is also a fatal() helper method for this level.
Both CRITICAL and FATAL share the same numeric log level of 50. They can be used interchangeably.

WARN can also be used as a shortcut for WARNING. They mean the same thing.

NOTSET is a special constant that represents the lowest possible log severity level.
It has a value of 0. You should not log messages with this severity level.
It is used when configuring loggers in the logging hierarchy.

In this task, replace the logging level passed to basicConfig() with NOTSET.
You will notice the output is similar to DEBUG, since NOTSET is a lower level (0) it includes every level.
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
        logger.warn('Term greater than 50 years')

    mon_rate = get_current_rate(years) / 1200
    payments = years * 12
    logger.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate / (1 - math.pow((1 + mon_rate), -payments)))

    logger.debug('Calculated result is %f' % result)
    logger.debug('Leaving mortgage calculator')
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
