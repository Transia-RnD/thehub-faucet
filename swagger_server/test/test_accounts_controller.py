# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.xrpl_faucet_request import XrplFaucetRequest  # noqa: E501
from swagger_server.models.xrpl_faucet_response import XrplFaucetResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    destination: str = 'rhfbXVZP7JFTFwAuhoqmeXCjSdMyHo5Gc8'
    xrp_amount: str = '1000'

    def test_accounts_faucet(self):
        """Test case for accounts_faucet

        Account Faucet
        """
        body = XrplFaucetRequest(
            destination=self.destination,
            xrp_amount=self.xrp_amount
        )
        response = self.client.open(
            '/v1/accounts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    import unittest
    unittest.main()
