#!/usr/bin/env python

"""Unit tests for the Python Open311 API wrapper."""

import unittest

from mock import Mock

from open311 import open311
from open311 import Open311


class TestOpen311Init(unittest.TestCase):

    def test_Open311_empty_init(self):
        open_311 = Open311()
        self.assertEquals(open_311.api_key, '')
        self.assertEquals(open_311.endpoint, '')
        self.assertEquals(open_311.format, 'xml')
        self.assertEquals(open_311.jurisdiction, '')
        self.assertEquals(open_311.proxy, '')
        self.assertEquals(open_311.user_agent, 'Open311 Python Wrapper')

    def test_Open311_init_with_kwargs(self):
        open_311 = Open311(api_key='my_api_key', endpoint='http://test.com')
        self.assertEquals(open_311.api_key, 'my_api_key')
        self.assertEquals(open_311.endpoint, 'http://test.com')


if __name__ == '__main__':
    unittest.main()
