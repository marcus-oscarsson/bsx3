# -*- coding: utf-8 -*-
""" Authentication and login related functionality """
from backend.bsxapp import get_app


def login():
    """ Login example routine """
    print(get_app().COUNTER)
