#!/usr/bin/env python
"""
Author: Zach Williams, <zach AT codeforamerica DOT org>

Copyright (c) 2011, Code for America. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
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
"""

setup(name="open311",
      version="1.1",
      description="A Python API wrapper for the Open311 API v2.",
      long_description=long_description,
      keywords="open311, Open311",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/open311_python",
      license="BSD",
      packages=['open311', 'open311.api', 'open311.api.xml2dict'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test_open311.py",
      tests_require=["mock", "Mock"])
