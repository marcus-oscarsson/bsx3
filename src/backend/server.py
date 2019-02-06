# -*- coding: utf-8 -*-
import logging

from aiohttp import web
from . routes import home, auth, counter
from . bsxapp import init_app


def init_backend():
    app = web.Application()

    logging.basicConfig(level=logging.DEBUG)
    app.add_routes(home.routes)
    app.add_routes(auth.routes)
    app.add_routes(counter.routes)
    init_app()

    return app


def run_server():
    app = init_backend()
    web.run_app(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    run_server()
