"""4-in-1 Kakao SDK server (infodesk, kauth, kapi, openapi)"""

import base64
import hashlib
import hmac
import json
import re
import time
import zlib
from wsgiref.simple_server import make_server

# Port used by the Kakao SDK server
_port = 8080

_request_country = 'kr'


def application(environ, start_response):
    # print('\n'.join([str((f'{key}: {value}').encode('utf-8'))
    #                  for key, value in environ.items()]))

    status = '200 OK'
    headers = [('Content-Type', 'application/json;charset=utf-8')]
    path_info = environ['PATH_INFO']
    if '/v2/app' in path_info:
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
                        # 'gameServerAddr': 'http://live.bdk.kakaogames.com:50051/api/',
                        'gameServerAddr': 'http://192.168.0.50:5000/api/',
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
        headers.append(('sig', f'0;{sig}'))
    elif 'oauth/authorize' in path_info:
        # query_string = environ['QUERY_STRING']
        # redirect_uri = re.search('redirect_uri=(.*%3A%2F%2Foauth)', query_string).group(1)
        # redirect_uri = redirect_uri.replace('%3A%2F%2F', '://') + '?code=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        # print(redirect_uri)
        status = '302 Found'
        # headers = [('Location', redirect_uri)]
        headers = [('Location', 'kakao00000000000000000000000000000000://oauth?code=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')]
        response = ''
    elif 'oauth/token' in path_info:
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
    elif 'v2/user/me' in path_info:
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
    elif 'v1/api/talk/profile' in path_info:
        status = '400 Bad Request'
        response = json.dumps(
            {
                'msg': 'given account is not connected to any talk user.',
                'code': -501
            },
            separators=(',', ':')
        )
    elif 'service/v3/agreement/getForLogin' in path_info:
        request_len = int(environ['CONTENT_LENGTH'])
        request = json.loads(environ['wsgi.input'].read(request_len))
        print(request)
        response = json.dumps(
            {
                'country': request['country'],
                'agreement': {
                    'E001': 'y',
                    'E002': 'y',
                    'E006': 'y',
                    'N002': 'y',
                    'N003': 'y',
                    'timestamp': int(time.time()*1000)
                },
                'partnerName': 'Kakao Games Corp.',
                'idpId': request['idpId'],
                'appName': '뱅드림! 걸즈 밴드 파티!',
                'adAgreementStatus': 'n',
                'policyApplyTime': None,
                'agreementPopup': 'n',
                'kakaoSyncAgreementGetSet': 'n',
                'firstAgreement': 'n',
                'informationSecurityCountry': 'kr',
                'kakaoSyncStatus': 'off',
                'plusFriendStatusInfo': None,
                'appId': request['appId'],
                'context': 'login',
                'partnerId': 825,
                'lang': request['lang'],
                'idpCode': request['idpCode'],
                'kakaogameSdkVer': '3.0'
            },
            separators=(',', ':')
        )
        headers.append(('reqTime', str(int(time.time()*1000))))
        headers.append(('backendReqTime', str(int(time.time()*1000))))
        headers.append(('startTime', str(int(time.time()*1000))))
        headers.append(('resTime', str(int(time.time()*1000))))
    elif '/service/v3/util/country/get' in path_info:
        response = f'{{"country":"{_request_country}"}}'
    elif 'v1/user/access_token_info' in path_info:
        response = json.dumps(
            {
                'expiresInMillis': 86_400_000,
                'id': 1000000000,
                'expires_in': 86_400,
                'app_id': 137316,
                'appId': 137316
            },
            separators=(',', ':')
        )
    elif '/session' in path_info:
        # print('\n'.join([str((f'{key}: {value}').encode('utf-8'))
        #                  for key, value in environ.items()]))
        query_string = environ['QUERY_STRING']
        prereq = re.search('prereq=(.*)', query_string).group(1)
        prereq = base64.urlsafe_b64decode(prereq)
        prereq = zlib.decompress(prereq)
        prereq = json.loads(prereq)
        print(f'{prereq=}')
        response = json.dumps(
            [
                prereq[0],
                prereq[1],
                {
                    'status': 200,
                    'desc': 'OK',
                    'content': {}
                }
            ],
            separators=(',', ':')
        ).encode('utf-8')
        response = zlib.compress(response)

        sec_websocket_key = environ['HTTP_SEC_WEBSOCKET_KEY']
        session_accept_magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        accept = (sec_websocket_key + session_accept_magic).encode('ascii')
        accept = hashlib.sha1(accept).digest()
        accept = base64.b64encode(accept)
        headers = [
            ('Content-Type', 'application/octet-stream'),
            ('Connection', 'Upgrade'),
            ('Upgrade', 'websocket'),
            ('Sec-WebSocket-Accept', str(accept))
        ]
    elif '/service/v3/log/writeSdkBasicLog' in path_info:
        request_len = int(environ['CONTENT_LENGTH'])
        print(environ['wsgi.input'].read(request_len))
        response = ''
    else:
        print(f'{environ["HTTP_HOST"]=}, {path_info=}')
        status = '503 Service Unavailable'
        headers = [('Content-Type', 'text/html')]
        response = '503 Service Unavailable'

    headers.append(('Content-Length', str(len(response))))
    start_response(status, headers)
    if isinstance(response, bytes):
        return [response]
    else:
        return [bytes(response, 'utf-8')]


def start(port):
    with make_server('', port, application) as httpd:
        print(f'Serving HTTP on port {port}...')
        httpd.serve_forever()


if __name__ == '__main__':
    start(_port)

