#!/usr/bin/env python
from gevent import monkey
monkey.patch_all(thread=False)

from backend import server

flask_app, socketio = server.init_backend()

if __name__ == '__main__':
    socketio.run(flask_app, host='0.0.0.0', port=8080, debug=True)
