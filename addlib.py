#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

@unittest.skip("Framework is OK")
class FrameworkIsWorking(unittest.TestCase):
    """Check the unittest framework is working."""

    def test_PassingTest(self):
        self.assertEqual(1,1)

    def test_FailingTest(self):
        self.assertEqual('2+2', 'fish')

def add5(augmenticand):
    return 5+augmenticand

class DevelopSomeLibFunction(unittest.TestCase):
    """TDD a library function."""

    def test_add5_returns_5_given_0(self):
        self.assertEqual(5, add5(0))

    def test_add5_returns_6_given_1(self):
        self.assertEqual(6, add5(1))


if __name__ == '__main__':
    print("add5() adds 5 to a number.")
    print("Tests:")
    print("------")
    unittest.main()
