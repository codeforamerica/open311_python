#!/usr/bin/env python

"""Unit tests for the Python Open311 API wrapper."""

import unittest

from mock import Mock

from open311.api import api
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
        endpoint = 'http://api.dc.org/open311/v2_dev'
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


class TestServiceListMethod(unittest.TestCase):

    def setUp(self):
        xml_services = """<?xml version="1.0" encoding="utf-8"?>
        <services>
            <service>
                <service_code>001</service_code>
                <service_name>Cans left out 24x7</service_name>
                <description>Garbage or recycling cans that have been left out for more than 24 hours after collection. Violators will be cited.</description>
                <metadata>true</metadata>
                <type>realtime</type>
                <keywords>lorem, ipsum, dolor</keywords>
                <group>sanitation</group>
            </service>
            <service>
                <service_code>002</service_code>
                <metadata>true</metadata>
                <type>realtime</type>
                <keywords>lorem, ipsum, dolor</keywords>
                <group>street</group>
                <service_name>Construction plate shifted</service_name>
                <description>Metal construction plate covering the street or sidewalk has been moved.</description>
            </service>
            <service>
                <service_code>003</service_code>
                <metadata>true</metadata>
                <type>realtime</type>
                <keywords>lorem, ipsum, dolor</keywords>
                <group>street</group>
                <service_name>Curb or curb ramp defect</service_name>
                <description>Sidewalk curb or ramp has problems such as cracking, missing pieces, holes, and/or chipped curb.</description>
            </service>
        </services>"""
        api.urlopen = Mock()
        api.urlopen().read.return_value = xml_services
        api.json = Mock()

    def test_service_list_method(self):
        endpoint = 'http://api.dc.org/open311/v2_dev'
        data = Open311(endpoint=endpoint).service_list()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))
        self.assertEquals(len(data), 3)


class TestServiceDefinitionMethod(unittest.TestCase):

    def setUp(self):
        xml_service_definition = """<?xml version="1.0" encoding="utf-8"?>
        <service_definition>
            <service_code>033</service_code>	
            <attributes>
                <attribute>
                    <variable>true</variable>
                    <code>WHISHETN</code>
                    <datatype>singlevaluelist</datatype>
                    <required>true</required>
                    <datatype_description></datatype_description>		
                    <order>1</order>	
                    <description>What is the ticket/tag/DL number?</description>
                    <values>
                        <value>
                            <key>123</key>
                            <name>Ford</name>
                        </value>
                        <value>
                            <key>124</key>
                            <name>Chrysler</name>
                        </value>			
                    </values>
                </attribute>	
            </attributes>
        </service_definition>"""
        api.urlopen = Mock()
        api.urlopen().read.return_value = xml_service_definition
        api.json = Mock()

    def test_default_service_definition_method(self):
        endpoint = 'http://api.dc.org/open311/v2_dev'
        open_311 = Open311(endpoint=endpoint, jurisdiction='dc.org')
        data = open_311.service_definition('033')
        expected_url = ('http://api.dc.org/open311/v2_dev/service/'
                        '033.xml?jurisdiction_id=dc.org')
        api.urlopen.assert_called_with(expected_url)
        self.assertTrue(isinstance(data, dict))


if __name__ == '__main__':
    unittest.main()
