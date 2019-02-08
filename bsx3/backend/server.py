# -*- coding: utf-8 -*-
from flask import Flask
from flask_socketio import SocketIO

from bsx3.backend.routes import home, auth, counter
from bsx3.backend.bsxapp import init_app


def init_backend():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(home.api, url_prefix='')
    flask_app.register_blueprint(auth.api, url_prefix='/auth')
    flask_app.register_blueprint(counter.api, url_prefix='/counter')
    init_app()

    socketio = SocketIO(manage_session=False)
    socketio.init_app(flask_app)

    return flask_app, socketio
