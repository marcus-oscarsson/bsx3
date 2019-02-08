# -*- coding: utf-8 -*-
""" Root route """

from flask import Blueprint, Response

api = Blueprint('home_api', __name__)


@api.route('/')
def index():
    """ root route """
    return Response("HOME", status=200)
