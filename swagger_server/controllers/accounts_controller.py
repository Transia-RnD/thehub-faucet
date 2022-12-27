import connexion
import os

from swagger_server.models.xrpl_faucet_request import XrplFaucetRequest  # noqa: E501
from swagger_server.models.faucet_account import FaucetAccount  # noqa: E501
from swagger_server.models.xrpl_faucet_response import XrplFaucetResponse  # noqa: E501
from swagger_server import util

from xrpl.clients import WebsocketClient
from xrpl.wallet import Wallet
from xrpl.models.transactions.payment import Payment
from xrpl.transaction import (
    safe_sign_and_autofill_transaction,
    send_reliable_submission
)
from xrpl.utils import xrp_to_drops

w3 = WebsocketClient(os.environ['XRPL_FAUCET_URL'])


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

        wallet: Wallet = Wallet(os.environ['XRPL_FAUCET_SEED'], 0)
        with w3 as client:
            drop_value = xrp_to_drops(float(body.xrp_amount))
            send_token_tx = Payment(
                account=wallet.classic_address,
                destination=body.destination,
                amount=drop_value
            )
            pay_prepared = safe_sign_and_autofill_transaction(
                transaction=send_token_tx,
                wallet=wallet,
                client=client,
            )
            response = send_reliable_submission(pay_prepared, client)

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
