#!/usr/bin/env python

"""
A Python wrapper for the Open311 API. This wrapper tries to mimic the Ruby
Open311 API wrapper as closely as possible.
"""

from collections import defaultdict

from api import API
from api.api import urlopen, urlencode


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

    def reset(self):
        """Reset the class to the original keywords passed to it."""
        self.configure()

    def service_list(self):
        """Return the service list for the given Open311 API."""
        data = self.call_api('services.xml', jurisdiction_id=self.jurisdiction)
        return data['services']['service']

    def service_definition(self, definition_number):
        """Return the service definition for a specific definition number."""
        if isinstance(definition_number, int):
            definition_number = str(definition_number)
        url_path = ''.join(['service/', definition_number, '.', self.format])
        data = self.call_api(url_path, jurisdiction_id=self.jurisdiction)
        return data

    def service_requests(self, **kwargs):
        """Return the service request resources."""
        url_path = ''.join(['requests', '.', self.format])
        kwargs.update({'jurisdiction_id': self.jurisdiction})
        data = self.call_api(url_path, **kwargs)
        return data['service_requests']['request']

    def get_service_request(self, request_number):
        """Return the service request for a specific number."""
        if isinstance(request_number, int):
            request_number = str(request_number)
        url_path = ''.join(['requests/', request_number, '.', self.format])
        data = self.call_api(url_path, jurisdiction_id=self.jurisdiction)
        return data

    def post_service_request(self, **kwargs):
        """Post data to an Open311 service."""
        params = urlencode({
            'jurisdiction_id': self.jurisdiction,
            'api_key': self.api_key
        })
        url_list = [self.endpoint, '/requests', '.', self.format, '?', params]
        url_path = ''.join(url_list)
        post_data = urlencode(kwargs)
        data = urlopen(url_path, post_data).read()
        formatted_data = self._format_data(self.format, data)
        return formatted_data

    def request_id_from_token(self, token_number):
        """Call for a request id by passing in a token."""
        if isinstance(token_number, int):
            token_number = str(token_number)
        url_path = ''.join(['tokens/', token_number, '.', self.format])
        data = self.call_api(url_path, jurisdiction_id=self.jurisdiction)
        return data['service_requests']['request']
