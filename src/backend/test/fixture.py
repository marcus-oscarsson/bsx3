# -*- coding: utf-8 -*-
""" Helper functions for pytest """
import pytest

from backend import server


@pytest.fixture
def client(loop, aiohttp_client):
    """PyTest fixture for REST API"""
    app = server.init_backend()
    return loop.run_until_complete(aiohttp_client(app))
