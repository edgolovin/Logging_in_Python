"""
In the previous task, only the application output was written to standard output.
You do not see any of the debugging statements.

There is no output because a default "Logger" instance was created for you by the "logging" module and
the logging level was set to WARNING level. This default "Logger" is also known as the "root" Logger.

The WARNING level is an example of how we can tag our log statements with a severity level and
perform filtering based on the level.

The "basicConfig()" function is a helper method for doing basic configuration of logging.
Without any parameters, it will create a StreamHandler that writes logging output to the "stderr" output stream.
We can also pass a keyword argument "level" to set the default logger level.

In this task using "basicConfig()", set the logging level to a value of "logging.DEBUG".
This will allow our debug statements to show up on stderr.
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
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
