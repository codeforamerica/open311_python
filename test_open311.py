#!/usr/bin/env python

"""Unit tests for the Python Open311 API wrapper."""

import unittest

from mock import Mock

from open311 import open311
from open311 import Open311


class TestOpen311Init(unittest.TestCase):

    def test_Open311_init(self):
        Open311()


if __name__ == '__main__':
    unittest.main()
