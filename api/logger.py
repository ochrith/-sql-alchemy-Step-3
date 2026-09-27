import logging
from flask import request


def setup_logger(app):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    file_handler = logging.FileHandler('logger.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    @app.before_request
    def before_request():
        client_ip = request.remote_addr
        path = request.path
        method = request.method
        query_params = request.args.to_dict()

        logger.info(
            f"IP: {client_ip} | {method} {path}"
        )





