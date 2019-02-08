# -*- coding: utf-8 -*-
""" Test for root routes """


async def test_home(client):
    """Test root route"""
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'HOME' in resp.data.decode()
