#!/usr/bin/env python

"""
A Python wrapper for the Open311 API. This wrapper tries to mimic the Ruby
Open311 API wrapper as closely as possible.
"""

from collections import defaultdict
from xml.etree import ElementTree

from api import API


class Open311(API):
    """A Python wrapper for the Open311 API."""

    def __init__(self, **kwargs):
        super(Open311, self).__init__()
        kwargs_or_str = defaultdict(str)
        for k, v in kwargs.items():
            kwargs_or_str[k] = v
        self._kwargs = kwargs_or_str
        self.configure()
        self.base_url = self.endpoint
        self.output_format = self.format
        self.required_params = None

    def configure(self, **kwargs):
        """
        Configure the Open311 class to either the original keyword arguments
        passed to it or the ones passed into the function.
        """
        keywords = self._kwargs.copy()
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

    def service_list(self):
        """Return the service list for the given Open311 API."""
        data = self.call_api('services.xml', jurisdiction_id=self.jurisdiction)
        return data['services']['service']

    def service_definition(self, definition_number):
        """Return the service definition for a specific definition number."""
        url_path = ''.join(['service/', definition_number, '.', self.format])
        data = self.call_api(url_path, jurisdiction_id=self.jurisdiction)
        return data
