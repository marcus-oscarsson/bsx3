# -*- coding: utf-8 -*-
""" Helper functions for pytest """
import pytest

from backend import server


@pytest.fixture
def client():
    """PyTest fixture for REST API"""
    flask_app, socketio = server.init_backend()
    client = flask_app.test_client()

    yield client
