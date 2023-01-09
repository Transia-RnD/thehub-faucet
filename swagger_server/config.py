#!/usr/bin/env python
# coding: utf-8

import os
import json
from typing import Dict, Any
from dotenv import dotenv_values

from google.cloud.secretmanager import SecretManagerServiceClient
from swagger_server.basedir import basedir

# APP ENV
APP_ENV = os.environ.get('APP_ENV', 'config.DevelopmentConfig')
PORT = os.environ.get('PORT', 9000)


class GCPSecretClient(object):
    """
    This class is used to load secrets from Google Secret Manager
    """

    project_id: str = None
    parent: str = None
    client: SecretManagerServiceClient = None

    def __init__(cls):
        """
        Initialize the class with project_id, version and gmail_version
        """
        cls.project_id = 'metaxrplorer'
        cls.parent = f'projects/{cls.project_id}'
        cls.client: SecretManagerServiceClient = SecretManagerServiceClient()

    def load_secrets(cls):
        """
        Load secrets
        :return: secrets
        """
        name = cls.parent + f'/secrets/FAUCET_SECRETS/versions/latest'
        return json.loads(cls.decrypt_key_value(name))

    def decrypt_key_value(cls, name=None):
        """
        Decrypt the key value
        :param name: name of the secret
        :return: decrypted value
        """
        response = cls.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("utf-8")


class Config(object):
    """Config."""

    def get_app_var(configs: Dict[str, Any], key):
        """get_app_var."""
        try:
            val = configs[key]
            if val == 'True':
                val = True
            elif val == 'False':
                val = False
            return val
        except KeyError:
            error_msg = f"ImproperlyConfigured: Set {key} environment variable"  # noqa
            raise ValueError(error_msg)

    ecyp_configs: Dict[str, Any] = GCPSecretClient().load_secrets()
    XRPL_FAUCET_SEED = get_app_var(ecyp_configs, 'XRPL_FAUCET_SEED')
    ecyp_configs = None