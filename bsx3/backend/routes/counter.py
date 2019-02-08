# -*- coding: utf-8 -*-
""" Counter routes
"""
from flask import Blueprint, jsonify

from bsx3.backend.bsxapp import counter

api = Blueprint('counter_api', __name__)


@api.route("increment", methods=["POST"])
def increment():
    """ Increment counter.

        Returns:
        JSON Response

        { counter: (int) count }
    """
    resp = jsonify({"counter": counter.increment()})
    resp.status_code = 200
    return resp


@api.route("decrement", methods=["POST"])
def decrement():
    """ Decrements counter.

        Returns:
        JSON Response

        { counter: (int)
     """
    resp = jsonify({"counter": counter.decrement()})
    resp.status_code = 200
    return resp


@api.route("get-count", methods=["POST"])
def get_count():
    """ Return current count.

        Returns:
        JSON Response

        { counter: (int)
     """
    resp = jsonify({"counter": counter.count()})
    resp.status_code = 200
    return resp
