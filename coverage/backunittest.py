# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""Implementations of unittest features from the future."""

import unittest


def unittest_has(method):
    """Does `unittest.TestCase` have `method` defined?"""
    return hasattr(unittest.TestCase, method)


class TestCase(unittest.TestCase):
    """Just like unittest.TestCase, but with assert methods added.

    Designed to be compatible with 3.1 unittest.  Methods are only defined if
    `unittest` doesn't have them.

    """
    # pylint: disable=signature-differs

    if not unittest_has('assertCountEqual'):
        def assertCountEqual(self, *args, **kwargs):
            return self.assertItemsEqual(*args, **kwargs)
