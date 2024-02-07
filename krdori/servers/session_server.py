"""Kakao session server"""

import asyncio
import base64
import hashlib
import hmac
import json
import logging
import pathlib
import re
import ssl
import time
import zlib

from websockets.datastructures import Headers
from websockets.http11 import Request, Response
# from websockets.sync.server import serve, ServerConnection
from websockets.server import serve

# Port used by the session server
_port = 8443

_session_accept_magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


# def process_request(websocket: ServerConnection, request: Request) -> Response | None:
async def process_request(path, request_headers) -> Response | None:
    # print(websocket)
    # print(request)
    print(path)
    print(request_headers)
    # path = request.path
    # request_headers = request.headers
    status_code = 200
    reason_phrase = 'OK'
    headers = Headers()
    headers['Content-Type'] = 'application/json;charset=utf-8'
    if 'v2/app' in path:
        response = json.dumps(
            {
                'status': 200,
                'desc': 'OK',
                'content': {
                    'supportedFeatures': [
                        'urgentNotice',
                        'maintenance',
                        'push',
                        'delivery',
                        'promotion',
                        'coupon',
                        'notice',
                        'leaderboard',
                        'community'
                    ],
                    'marketUrl': 'market://details?id=com.kakaogames.bangdreamkr',
                    'publicKeyMap': {},
                    'secondaryPwOption': None,
                    'capriAppOption': {
                        'ageLimit': 0,
                        'lazyAgeAuth': None,
                        'appType': 'LEGACY_PARTNER',
                        'appCategory': 'Games',
                        'ageAuthLevel': 'NONE'
                    },
                    'isTubeApp': False,
                    'verRecent': '6.5.2',
                    'appOption': {
                        'cdnAddr': 'https://bandori-assets.rainbowunicorn7297.com/kr/',
                        'agreementUrl': 'https://web-data-game.kakaocdn.net/real/www/html/agreement/index.html',
                        'useGoogleGame': 'true',
                        'PassWebUrl': 'https://www.kakao.com',
                        'url_star_shop_help': 'https://kakaogames.oqupie.com/portals/1697/articles/35886',
                        'photonchatId': 'd5eb7ab5-9976-4dd9-974d-a36b9139c6b9',
                        'static-web': 'http://patch-gs.bdk.kakaogames.com/live/static-web',
                        'url_setting_dialog_help': 'https://kakaogames.oqupie.com/portals/1697/articles/35835',
                        'kakaogameCommunityUrl': 'https://playgame.kakao.com/bangdream',
                        'gameServerAddr': 'http://live.bdk.kakaogames.com:50051/api/',
                        'modTime': 1514876083602,
                        'daumCafeUrl': 'http://cafe.daum.net/bangdream',
                        'photonId': 'abb90c74-f36d-441b-bf5d-241315ea5f06',
                        'RefundWebUrl': 'https://cs.kakao.com/helps?category=354&amp;device=1077&amp;locale=ko&amp;service=4&amp;articleId=1073190458&amp;page=1'
                    },
                    'notices': [],
                    'traceSampleRate': 0,
                    'isWhitelist': False,
                    'svcStatus': 'open',
                    'supportedIdpCodes': [
                        'kakaocapri',
                        'zd3'
                    ],
                    'serverConnectionType': 'wss',
                    'appVerStatus': 'noNeedToUpdate',
                    'publisher': {
                        'privacyUrl': 'https://www.kakao.com/ko/privacy',
                        'privacySummaryUrl': 'https://gameevent.kakao.com/supports/terms/3?tabbar=false',
                        'noticeUrl2': 'https://cus-zinny3.kakaogames.com/view/notice',
                        'agreementUrl': 'https://web-data-game.kakaocdn.net/real/www/html/agreement/index.html?tid=13',
                        'servicePolicyUrl': 'https://gameevent.kakao.com/terms/operation',
                        'termsUrl': 'https://gameevent.kakao.com/supports/terms/1',
                        'kakaogameCommunityUrl': 'https://playgame.kakao.com/bridge/auth/zinny',
                        'termsSummaryUrl': 'https://gameevent.kakao.com/supports/terms/1?tabbar=false',
                        'eventWallUrl': 'https://cus-zinny3.kakaogames.com/view/event',
                        'noticeUrl': 'https://cus-zinny3.kakaogames.com/notice',
                        'customerServiceUrl': 'https://cus-zinny3.kakaogames.com/support/list',
                        'eventWinnerUrl': 'http://event-winner.kakaogames.com/event',
                        'policyVer': '1.0',
                        'publisherId': 'kakao',
                        'modTime': 1651813742832
                    },
                    'sdk': {
                        'heartbeatInterval': 120000,
                        'PercentOfSendingAPICallLog': 0,
                        'stopSendGeoDNS': 'y',
                        'snsShareUrl': 'https://invite.kakaogame.com',
                        'zrtiOSError': '{"kakaocapri":[500, 502, 503, -1, -7, -9]}',
                        'aesEncryptKey': 'djfdskj12328438djdgjcjeejhdew15',
                        'aesEncryptIV': '7gnfn7f96rnanmt1s5iaa3kdruhuneu',
                        'cafeLoginUrl': 'https://accounts.kakao.com/weblogin/sso_login?token={tgt_token}&token_type=tgt&continue={url}',
                        'zrtAOSError': '{"kakaocapri":[500, 502, 503, -1, -7, -9],"google":[8]}',
                        'zrtWindowsError': '{"kakaocapri":[500, 502, 503, -1, -7, -9]}',
                        'snsShareHostUrl': 'https://invite.kakaogame.com/host/main',
                        'invitationUrl': 'https://webinvite.nzincorp.com',
                        'csUrl': 'http://customer.kakaogames.com:18080',
                        'platformVersion': 3,
                        'sessionTimeout': 10000,
                        'registerDeviceUrl': 'https://device-enrollment.kakaogames.com/main',
                        'customDialogModels': ['SM-T976N'],
                        'unregisterAgreementUrl': 'https://web-data-cdn.kakaogames.com/real/www/html/terms/index.html?service=S0001&type=T016',
                        'snsShareGuestUrl': 'https://invite.kakaogame.com/guest/reward'
                    },
                    'deviceSecurityOption': None,
                    'onlineNotifications': [],
                    'timestamp': int(time.time()*1000)
                }
            },
            separators=(',', ':')
        )
        response_bytes = bytes(response, 'utf-8')
        infodesk_secret = b'qvjNK+TlAJ'
        sig = hmac.digest(infodesk_secret, response_bytes, hashlib.sha256)
        sig = base64.b64encode(sig).decode('ascii')
        headers['sig'] = f'0;{sig}'
    elif 'oauth/authorize' in path:
        print('oauth/authorize')
        status_code = 302
        reason_phrase = 'Found'
        headers = Headers()
        headers['Location'] = 'kakao00000000000000000000000000000000://oauth?code=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        response = ''
    elif 'oauth/token' in path:
        response = json.dumps(
            {
                'access_token': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                'token_type': 'bearer',
                'refresh_token': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                'expires_in': 43199,
                'scope': 'profile',
                'refresh_token_expires_in': 5183999
            },
            separators=(',', ':')
        )
    elif 'v2/user/me' in path:
        response = json.dumps(
            {
                'id': 1000000000,
                'connected_at': '2000-01-01T00:00:00Z',
                'has_signed_up': True,
                'for_partner': {
                    'uuid': 'AAAAAAAAAAAAAAAAAAAAAAAAAAA',
                    'remaining_invite_count': 30,
                    'remaining_group_msg_count': 10
                },
                'properties': {
                    'nickname': 'KRdori',
                    'profile_image': 'https://bandori-assets.rainbowunicorn7297.com/kr/img_640x640.jpg',
                    'thumbnail_image': 'https://bandori-assets.rainbowunicorn7297.com/kr/img_110x110.jpg'
                },
                'kakao_account': {
                    'profile_needs_agreement': False,
                    'profile': {
                        'nickname': 'KRdori',
                        'thumbnail_image_url': 'https://bandori-assets.rainbowunicorn7297.com/kr/img_110x110.jpg',
                        'profile_image_url': 'https://bandori-assets.rainbowunicorn7297.com/kr/img_640x640.jpg',
                        'is_default_image': True
                    },
                    'service_user_id': 100000000000000000
                }
            },
            separators=(',', ':')
        )
    elif 'v1/api/talk/profile' in path:
        status_code = 400
        reason_phrase = 'Bad Request'
        response = json.dumps(
            {
                'msg': 'given account is not connected to any talk user.',
                'code': -501
            },
            separators=(',', ':')
        )
    elif 'service/v3/agreement/getForLogin' in path:
        # request_len = int(request_headers['Content-Type'])
        # request = json.loads(request_headers['wsgi.input'].read(request_len))
        response = json.dumps(
            {
                # 'country': request['country'],
                'country': 'kr',
                'agreement': {
                    'E001': 'y',
                    'E002': 'y',
                    'E006': 'y',
                    'N002': 'y',
                    'N003': 'y',
                    'timestamp': int(time.time()*1000)
                },
                'partnerName': 'Kakao Games Corp.',
                'idpId': '1000000000',
                'appName': '뱅드림! 걸즈 밴드 파티!',
                'adAgreementStatus': 'n',
                'policyApplyTime': None,
                'agreementPopup': 'n',
                'kakaoSyncAgreementGetSet': 'n',
                'firstAgreement': 'n',
                'informationSecurityCountry': 'kr',
                'kakaoSyncStatus': 'off',
                'plusFriendStatusInfo': None,
                'appId': '137316',
                'context': 'login',
                'partnerId': 825,
                'lang': 'en',
                'idpCode': 'kakaocapri',
                'kakaogameSdkVer': '3.0'
            },
            separators=(',', ':')
        )
        # headers.append(('reqTime', str(int(time.time()*1000))))
        # headers.append(('backendReqTime', str(int(time.time()*1000))))
        # headers.append(('startTime', str(int(time.time()*1000))))
        # headers.append(('resTime', str(int(time.time()*1000))))
    elif '/service/v3/util/country/get' in path:
        response = '{"country":"kr"}'
    else:
        return None
    headers['Content-Length'] = str(len(response))
    print(f'{status_code}, {headers}, {response}')
    if isinstance(response, bytes):
        return Response(status_code, reason_phrase, headers, response)
    else:
        return Response(status_code, reason_phrase, headers, bytes(response, 'utf-8'))


# def process_response(websocket: ServerConnection, request: Request, response: Response) -> Response | None:
#     print('in process_response')
#     return None


async def handler(websocket):
    async for message in websocket:
        # if websocket.response:
        #     continue
        # print(websocket.request.headers)
        print(message)
        await websocket.send(message)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
certfile = pathlib.Path(__file__).with_name('gc-session-zinny3.crt')
keyfile = pathlib.Path(__file__).with_name('gc-session-zinny3.key')
ssl_context.load_cert_chain(certfile, keyfile)


async def main(port):
    # async with serve(handler, '', 8081, process_request=process_request):
    async with serve(handler, '', port, ssl=ssl_context, process_request=process_request):
        print(f'Serving WSS on port {port}...')
        await asyncio.Future()  # run forever


# def sync_handler(websocket):
#     for message in websocket:
#         print(message)
#         websocket.send(message)


if __name__ == '__main__':
    try:
        # with serve(handler, '', 8081, ssl_context=ssl_context, process_request=process_request, process_response=process_response) as server:
        #     # server.socket.accept()
        #     server.serve_forever()
        asyncio.run(main(_port))
        # with serve(sync_handler, '', 8443, ssl_context=ssl_context) as server:
        #     server.socket.accept()
    except KeyboardInterrupt:
        pass

