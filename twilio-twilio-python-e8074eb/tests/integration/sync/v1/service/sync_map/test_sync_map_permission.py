# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SyncMapPermissionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_map_permissions(identity="identity").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Permissions/identity',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "identity",
                "read": true,
                "write": true,
                "manage": true,
                "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions/identity"
            }
            '''
        ))

        actual = self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_map_permissions(identity="identity").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_map_permissions(identity="identity").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Permissions/identity',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_map_permissions(identity="identity").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_map_permissions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Permissions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "permissions": [],
                "meta": {
                    "first_page_url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/sidOrUniqueName/Permissions?PageSize=50&Page=0",
                    "key": "permissions",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/sidOrUniqueName/Permissions?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_map_permissions.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "permissions": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "identity": "identity",
                        "read": true,
                        "write": true,
                        "manage": true,
                        "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions/identity"
                    }
                ],
                "meta": {
                    "first_page_url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/sidOrUniqueName/Permissions?PageSize=50&Page=0",
                    "key": "permissions",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/sidOrUniqueName/Permissions?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_map_permissions.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                               .sync_map_permissions(identity="identity").update(read=True, write=True, manage=True)

        values = {'Read': True, 'Write': True, 'Manage': True, }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Permissions/identity',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "identity",
                "read": true,
                "write": true,
                "manage": true,
                "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions/identity"
            }
            '''
        ))

        actual = self.client.sync.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_maps(sid="MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_map_permissions(identity="identity").update(read=True, write=True, manage=True)

        self.assertIsNotNone(actual)
