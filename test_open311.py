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


class TestConfigureMethod(unittest.TestCase):

    def test_configure_with_api_key_kwarg(self):
        open_311 = Open311()
        self.assertEquals(open_311.api_key, '')
        open_311.configure(api_key='my_api_key')
        self.assertEquals(open_311.api_key, 'my_api_key')

    def test_configure_with_multiple_kwargs(self):
        open_311 = Open311()
        self.assertEquals(open_311.endpoint, '')
        self.assertEquals(open_311.jurisdiction, '')
        endpoint = 'http://api.dc.org/open311/v2_dev/'
        open_311.configure(endpoint=endpoint, jurisdiction='dc.gov')
        self.assertEquals(open_311.endpoint, endpoint)
        self.assertEquals(open_311.jurisdiction, 'dc.gov')


class TestResetMethod(unittest.TestCase):

    def test_reset_method_restores_initial_properties(self):
        open_311 = Open311()
        open_311.configure(api_key='my_api_key')
        self.assertEquals(open_311.api_key, 'my_api_key')
        open_311.reset()
        self.assertEquals(open_311.api_key, '')


if __name__ == '__main__':
    unittest.main()
