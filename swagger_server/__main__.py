#!/usr/bin/env python3

import connexion
import os

from flask_cors import CORS
from swagger_server import encoder

from dotenv import load_dotenv
load_dotenv()

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Xrpl Faucet'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
