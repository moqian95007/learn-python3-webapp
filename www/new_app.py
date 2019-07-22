#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# aiohttp	3.5.4
from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
