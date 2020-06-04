"""
When you can organize logging into a hierarchy, you can easily change the logging level at any point in this structure.
This is a powerful way as narrowing your output to certain modules or subsystems.

You can change the level in this structure by obtaining the logger instance at that level and
calling the "setLevel" method with the desired log level.

In this task, obtain a reference to the "mortgage.rate" logger instance and set its level to DEBUG.
When we run this program, we will see all messages DEBUG level or higher for this logger.
"""
from __future__ import print_function
import math
import logging

logger = logging.getLogger('mortgage')


def get_current_rate(years):
    logger = logging.getLogger('mortgage.rate')

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
    logging.basicConfig(level=logging.WARNING)
    rate_logger = logging.getLogger('mortgage.rate')
    rate_logger.setLevel(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
