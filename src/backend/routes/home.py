# -*- coding: utf-8 -*-
""" Root route """

from aiohttp import web
from backend.bsxapp import auth

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    """ root route """
    auth.login()
    return web.Response(text="HOME")
