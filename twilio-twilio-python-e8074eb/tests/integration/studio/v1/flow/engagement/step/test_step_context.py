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


class StepContextTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v1.flows(sid="FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .engagements(sid="FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .steps(sid="FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .step_context().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://studio.twilio.com/v1/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Engagements/FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Steps/FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Context',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "context": {
                    "foo": "bar"
                },
                "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "engagement_sid": "FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "step_sid": "FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://studio.twilio.com/v1/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps/FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Context"
            }
            '''
        ))

        actual = self.client.studio.v1.flows(sid="FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .engagements(sid="FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .steps(sid="FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .step_context().fetch()

        self.assertIsNotNone(actual)
