# -*- coding: utf-8 -*-
""" Tests for counter routes """


async def test_increment(client):
    """ Tests increment count """
    resp = await client.post("/counter/get-count")
    assert resp.status == 200
    count_before = (await resp.json()).get("counter")

    resp = await client.post("/counter/increment")
    assert resp.status == 200

    resp = await client.post("/counter/get-count")
    assert resp.status == 200
    count_after = (await resp.json()).get("counter")

    assert count_after == (count_before + 1)
