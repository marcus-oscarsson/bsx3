# -*- coding: utf-8 -*-
""" Application wide functionality"""

# Application instance
APP = None


class Application():
    """ Encapsulates all application wide data """
    COUNTER = 1

    def __init__(self):
        pass


def init_app():
    """ Initializes the application instance """
    global APP

    if not APP:
        APP = Application()

    return APP


def get_app():
    """ Returns the application instance """
    return init_app()
