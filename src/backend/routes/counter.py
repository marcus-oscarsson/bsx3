# -*- coding: utf-8 -*-
""" Counter routes
"""

from aiohttp import web
from backend.bsxapp import counter

routes = web.RouteTableDef()


@routes.post("/counter/increment")
async def increment(request):
    """ Increment counter.

        Returns:
        JSON Response

        { counter: (int) count }
    """
    content = {"counter": counter.increment()}
    return web.json_response(content, status=200)


@routes.post("/counter/decrement")
async def decrement(request):
    """ Decrements counter.

        Returns:
        JSON Response

        { counter: (int)
     """
    content = {"counter": counter.decrement()}
    return web.json_response(content, status=200)


@routes.post("/counter/get-count")
async def get_count(request):
    """ Return current count.

        Returns:
        JSON Response

        { counter: (int)
     """
    content = {"counter": counter.count()}
    return web.json_response(content, status=200)
