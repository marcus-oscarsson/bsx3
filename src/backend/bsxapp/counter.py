# -*- coding: utf-8 -*-
""" Counter example module """

from backend.bsxapp import get_app


def increment():
    """ Increment counter """
    app = get_app()
    app.COUNTER += 1

    return app.COUNTER


def decrement():
    """ Decrement counter """
    app = get_app()
    app.COUNTER -= 1

    return app.COUNTER


def count():
    """ Get count """
    app = get_app()
    return app.COUNTER
