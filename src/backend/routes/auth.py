# -*- coding: utf-8 -*-
""" Auth module """

from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/auth/login")
async def login(request):
    """ Example login """
    content = {}
    return web.json_response(content, status=200)
