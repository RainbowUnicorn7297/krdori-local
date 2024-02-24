"""Kakao session server"""

import asyncio
import base64
import json
import logging
import re
import time
import zlib

from websockets.server import serve

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


async def handler(websocket):
    prereq = re.search('prereq=(.*)', websocket.path).group(1)
    prereq = base64.urlsafe_b64decode(prereq)
    prereq = zlib.decompress(prereq)
    prereq = json.loads(prereq)
    requestUri = prereq[0]
    header = json.dumps(
        {
            'txNo': prereq[1]['txNo']
        },
        separators=(',', ':')
    )
    body = json.dumps(
        {
            'status': 200,
            'desc': 'success',
            'content': {
                'player': {
                    'playerId': '900000000000',
                },
                'zat': 'zat',
                'zatExpiryTime': int(time.time()*1000) + 86_400_000,
            }
        },
        separators=(',', ':')
    )
    await websocket.send(f'["{requestUri}",{header},{body}]')
    async for message in websocket:
        print(message)
        request = json.loads(message)
        requestUri = request[0]
        if requestUri == 'presence://v2/player/heartbeat':
            await websocket.send(None)
        else:
            await websocket.send(message)


async def main(port):
    async with serve(handler, '', port):
        print(f'Running session server on port {port}...')
        await asyncio.Future()  # run forever

