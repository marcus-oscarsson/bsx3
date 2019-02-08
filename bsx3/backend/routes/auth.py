# -*- coding: utf-8 -*-
""" Auth module """

from flask import Blueprint, jsonify
from bsx3.backend.bsxapp import auth

api = Blueprint("auth_api", __name__)


@api.route("login", methods=["GET"])
def login():
    """ Example login """
    auth.login()
    resp = jsonify({})
    return resp
