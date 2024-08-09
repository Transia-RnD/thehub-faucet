import connexion
import os

from xrpl.clients import WebsocketClient
from xrpl.wallet import Wallet
from xrpl.models.transactions.payment import Payment
from xrpl.transaction import (
    autofill_and_sign,
    submit_and_wait
)
from xrpl.utils import xrp_to_drops

from swagger_server.config import Config

from swagger_server.models.xrpl_faucet_request import XrplFaucetRequest  # noqa: E501
from swagger_server.models.faucet_account import FaucetAccount  # noqa: E501
from swagger_server.models.xrpl_faucet_response import XrplFaucetResponse  # noqa: E501
from swagger_server import util


def accounts_faucet(body):  # noqa: E501
    """Account Faucet

     # noqa: E501

    :param body: Xrpl Faucet Payload
    :type body: dict | bytes

    :rtype: XrplFaucetResponse
    """
    try:
        if connexion.request.is_json:
            body = XrplFaucetRequest.from_dict(connexion.request.get_json())  # noqa: E501

        wallet: Wallet = Wallet.from_seed(os.environ['XRPL_FAUCET_SEED'])
        with WebsocketClient(os.environ['XRPL_FAUCET_URL']) as client:
            drop_value = xrp_to_drops(float(body.xrp_amount or 1000))
            send_token_tx = Payment(
                account=wallet.classic_address,
                destination=body.destination,
                amount=drop_value,
                network_id=int(os.environ.get('XRPL_NETWORK_ID', 21336)),
            )
            pay_prepared = autofill_and_sign(
                transaction=send_token_tx,
                client=client,
                wallet=wallet,
            )
            response = submit_and_wait(pay_prepared, client)

            if 'meta' not in response.result or response.result['meta']['TransactionResult'] != 'tesSUCCESS':
                raise ValueError('transaction was not successful')

            account: FaucetAccount = FaucetAccount(
                x_address=None,
                classic_address=body.destination,
                secret=None
            )
            return XrplFaucetResponse(
                account=account,
                amount=body.xrp_amount,
                balance=None
            )
    except Exception as e:
        raise e
