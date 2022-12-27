# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.faucet_account import FaucetAccount  # noqa: F401,E501
from swagger_server import util


class XrplFaucetResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account: FaucetAccount=None, amount: float=None, balance: float=None):  # noqa: E501
        """XrplFaucetResponse - a model defined in Swagger

        :param account: The account of this XrplFaucetResponse.  # noqa: E501
        :type account: FaucetAccount
        :param amount: The amount of this XrplFaucetResponse.  # noqa: E501
        :type amount: float
        :param balance: The balance of this XrplFaucetResponse.  # noqa: E501
        :type balance: float
        """
        self.swagger_types = {
            'account': FaucetAccount,
            'amount': float,
            'balance': float
        }

        self.attribute_map = {
            'account': 'account',
            'amount': 'amount',
            'balance': 'balance'
        }
        self._account = account
        self._amount = amount
        self._balance = balance

    @classmethod
    def from_dict(cls, dikt) -> 'XrplFaucetResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The XrplFaucetResponse of this XrplFaucetResponse.  # noqa: E501
        :rtype: XrplFaucetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account(self) -> FaucetAccount:
        """Gets the account of this XrplFaucetResponse.


        :return: The account of this XrplFaucetResponse.
        :rtype: FaucetAccount
        """
        return self._account

    @account.setter
    def account(self, account: FaucetAccount):
        """Sets the account of this XrplFaucetResponse.


        :param account: The account of this XrplFaucetResponse.
        :type account: FaucetAccount
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def amount(self) -> float:
        """Gets the amount of this XrplFaucetResponse.


        :return: The amount of this XrplFaucetResponse.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this XrplFaucetResponse.


        :param amount: The amount of this XrplFaucetResponse.
        :type amount: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def balance(self) -> float:
        """Gets the balance of this XrplFaucetResponse.


        :return: The balance of this XrplFaucetResponse.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        """Sets the balance of this XrplFaucetResponse.


        :param balance: The balance of this XrplFaucetResponse.
        :type balance: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance