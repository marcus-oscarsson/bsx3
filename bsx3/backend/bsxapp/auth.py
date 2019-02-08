# -*- coding: utf-8 -*-
""" Authentication and login related functionality """
from bsx3.backend.bsxapp import get_app


def login():
    """ Login example routine """
    print(get_app().COUNTER)
