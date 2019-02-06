# -*- coding: utf-8 -*-
""" Tests for counter routes """


def test_increment(client):
    """ Tests increment count """
    resp = client.post("/counter/get-count")
    assert resp.status_code == 200
    count_before = (resp.get_json()).get("counter")

    resp = client.post("/counter/increment")
    assert resp.status_code == 200

    resp = client.post("/counter/get-count")
    assert resp.status_code == 200
    count_after = (resp.get_json()).get("counter")

    assert count_after == (count_before + 1)
