#!/usr/bin/env python
# coding: utf-8

import os
import json
from typing import Dict, Any
from dotenv import dotenv_values

from swagger_server.basedir import basedir

# APP ENV
APP_ENV = os.environ.get('APP_ENV', 'config.DevelopmentConfig')
PORT = os.environ.get('PORT', 9000)

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

    ecyp_configs = None