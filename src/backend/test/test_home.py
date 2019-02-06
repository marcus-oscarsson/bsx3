# -*- coding: utf-8 -*-
""" Test for root routes """


async def test_home(client):
    """Test root route"""
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'HOME' in text
