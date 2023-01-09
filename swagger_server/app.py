#!/usr/bin/env python
# coding: utf-8

import connexion
import os

from swagger_server import encoder
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = connexion.App(__name__, specification_dir='./swagger/')
CORS(app.app)
app.app.json_encoder = encoder.JSONEncoder
app.add_api(
    'swagger.yaml',
    arguments={'title': 'Xrpl Faucet'},
    pythonic_params=True
)

# Main Flask App Run
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 9000)), debug=True)