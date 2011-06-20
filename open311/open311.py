#!/usr/bin/env python

"""
A Python wrapper for the Open311 API. This wrapper tries to mimic the Ruby
Open311 API wrapper as closely as possible.
"""

from collections import defaultdict

from api.api import urlopen


class Open311(object):

    def __init__(self, **kwargs):
        kwargs_or_str = defaultdict(str)
        for k, v in kwargs.items():
            kwargs_or_str[k] = v
        self._kwargs = kwargs_or_str
        self.configure()

    def configure(self, **kwargs):
        """
        Configure the Open311 class to either the original keyword arguments
        passed to it or the ones passed into the function.
        """
        keywords = self._kwargs
        keywords.update(kwargs)
        self.api_key = keywords['api_key']
        self.endpoint = keywords['endpoint']
        self.format = keywords['format'] or 'xml'
        self.jurisdiction = keywords['jurisdiction']
        self.proxy = keywords['proxy']
        self.user_agent = 'Open311 Python Wrapper'

    def reset(self):
        """Reset the class to the original keywords passed to it."""
        self.configure()
