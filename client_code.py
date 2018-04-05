#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import addlib

if __name__ == '__main__':
    print("addlib.add5() adds 5 to a number.")
    print("---------------------------------")
    print(
        "addlib.add5(2): {}\n"
        "addlib.add5(3): {}\n"
        "addlib.add5(5): {}\n"
        .format(
            addlib.add5(2),
            addlib.add5(3),
            addlib.add5(5)
            )
        )
