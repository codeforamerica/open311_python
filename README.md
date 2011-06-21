Open311 API Python Wrapper
==========================

A Python API wrapper for the Open311 API v2.


Usage
-----

The Python wrapper follows closely with the structure of the [Ruby
Open311 API wrapper](https://github.com/codeforamerica/open311).

    >>> from open311 import Open311
    >>> o = Open311()

    >>> # If you forgot to configure your instance.
    ... o.configure(endpoint='http://open311.endpoint.com',
    ...             api_key='my_api_key', jurisdiction='endpoint.com')

    >>> # You can also reset your instance to its original state.
    ... o.reset()

    >>> # Receive a list of services available -- in dictionary form.
    ... o.service_list()

    >>> # Specific service definition.
    ... o.service_definition('033')

    >>> # Service requests.
    ... o.service_requests()

    >>> # Get a specific service request.
    ... o.get_service_request('638344')

    >>> # Post a service request.
    ... o.post_service_request(
    ...     service_code='001', address_string='123 Any Street',
    ...     first_name='John', last_name='Smith',
    ...     phone='111-111-1111', email='me@email.com',
    ...     description='A large sinkhole is destroying the street',
    ...     media_url='http://imgur.com/123_street_sinkhole.png')

    >>> # Get a request id from a token.
    ... o.request_id_from_token('123456')


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
