"""Game API server"""

import json
import time
from operator import attrgetter

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flask import Flask, Request, request, Response

from krdori.pb2.ce import (
    app_pb2, server_system_pb2, suite_user_character_pb2,
    suite_user_event_story_memorial_pb2, suite_user_login_bonus_pb2,
    suite_user_pb2, user_action_set_album_pb2, user_area_pb2, user_auth_pb2,
    user_backstage_talk_set_pb2, user_band_story_pb2,
    user_event_story_memorial_pb2, user_pb2, user_story_pb2
)
# from krdori.pb2.ce import suite_user_story_pb2

app = Flask(__name__)

_suite_master = None
_suite_user = None

_key = b'bangdreamtokakao'
_iv = b'kakaotobangdream'


def encrypt(data: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    return cipher.encrypt(pad(data, AES.block_size, 'x923'))


def decrypt(data: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    decrypted = cipher.decrypt(data)
    padded_bytes = decrypted[-1]
    return decrypted[:-padded_bytes]


class GameRequest(Request):
    @property
    def data(self) -> bytes:
        if not super().data:
            return None
        return decrypt(super().data)


app.request_class = GameRequest


@app.after_request
def encrypt_response(response: Response) -> Response:
    if response.response:
        combined = bytearray()
        for b in response.response:
            combined.extend(b)
        encrypted = encrypt(bytes(combined))
        response.response = [encrypted]
        response.content_length = len(encrypted)
        response.content_type = 'application/octet-stream'
    return response


@app.post('/api/user/')
def post_user_api():
    i = user_pb2.UserPostRequest.FromString(request.data)
    o = user_pb2.UserRegistration()
    o.user_id = 1000000
    o.hash = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
    o.user_name = '신입 스태프'
    o.client_version = i.client_version
    o.platform = i.platform
    o.device_model = i.device_model
    o.operating_system = i.operating_system
    o.birth_month = '201802'
    o.tutorial_status = 'end'
    o.introduction = '잘 부탁드립니다!'
    o.unknown_string = 'standard'
    o.tutorial_ended_at = 1517886000000
    o.kakao_id = i.kakao_id
    o.kakao_guest_flg = i.kakao_guest_flg
    return o.SerializeToString()


@app.put('/api/user/<int:user_id>/auth/prepare')
def prepare_user_auth_api(user_id):
    o = user_auth_pb2.UserAuthPrepareResponse()
    o.api_key = 'A'*39
    o.nonce = 'A'*64
    o.need_check = True
    return o.SerializeToString()


@app.put('/api/user/<int:user_id>/auth')
def user_auth_api(user_id):
    return b''


@app.get('/api/application')
def get_app_api():
    o = app_pb2.AppGetResponse()
    o.client_version = '6.5.0-SNAPSHOT'
    o.data_version = '6.5.0.0'
    o.app_status = 'available'
    o.client_status = 'snapshot'
    o.schema = 'amaterasu'
    o.gacha = 'available'
    o.multi_live = 'available'
    o.star_shop = 'available'
    o.master_data_version = '6.5.47'
    o.photon_app_id = '4ddacf66-3d97-4cfa-ae56-1d92a6cb849b'
    return o.SerializeToString()


@app.get('/api/suite/master')
def get_suite_master_api():
    with open('krdori/responses/suite_master.bz2', 'rb') as f:
        o = f.read()
    return o, 200, [('X-Encoding', 'bzip2')]


@app.get('/api/suite/user/<int:user_id>')
def suite_user_api(user_id):
    global _suite_master, _suite_user

    with open('krdori/responses/suite_master.json', 'rb') as f:
        _suite_master = json.loads(f.read())

    o = suite_user_pb2.SuiteUserGetResponse()

    r = o.user.user_registration
    r.user_id = user_id
    r.hash = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
    r.user_name = '신입 스태프'
    r.client_version = '6.5.0-SNAPSHOT'
    r.platform = 'Android'
    r.device_model = 'samsung SM-S908N'
    r.operating_system = ('Android OS 9 / API-28 '
                          '(PQ3A.190705.003/G9700FXXU1APFO)')
    r.birth_month = '201802'
    r.tutorial_status = 'end'
    r.introduction = '잘 부탁드립니다!'
    r.unknown_string = 'standard'
    r.tutorial_ended_at = 1517886000000
    r.kakao_id = '900000000000'
    r.kakao_guest_flg = '0'
    # TODO
    g = o.user.user_gamedata
    g.user_id = user_id
    g.rank = 38
    g.exp = 1980
    g.coin = 2603500
    g.main_deck = 1
    g.paid_star = 0
    g.free_star = 70175
    g.seal = 0
    g.degree = 100
    g.publish_total_deck_power_flg = 0
    g.publish_band_rank_flg = 0
    g.publish_music_cleared_flg = 0
    g.publish_music_full_combo_flg = 0
    g.publish_high_score_rating_flg = 0
    g.pooled_exp = 0
    g.total_exp = 261900
    g.next_exp = 11380
    g.publish_updated_at_flg = 1
    g.unknown_bool_19 = 0
    g.unknown_bool_20 = 1
    g.unknown_bool_21 = 1
    g.start_dash_login_bonus_receive_flg = 1
    g.publish_music_all_perfect_flg = 0
    g.publish_deck_rank_flg = 0
    g.publish_stage_achievement_conditions_flg = 0
    g.publish_stage_friend_ranking_flg = 1

    for i in range(1, 36):
        c = o.user_character_map.entries[i]
        c.user_id = user_id
        c.character_id = i
        c.costume_id = i + 1332

    for m in _suite_master['4']['1']:   # MasterCharacterSituationMap
        if m['2']['17'] < 4102444800000:
            s = o.user_situation_map.entries[m['1']]
            s.user_id = user_id
            s.situation_id = m['1']
            s.level = m['2']['11'] + (
                m['2']['15']['3'] if '15' in m['2'] else 0)
            s.exp = 0
            s.created_at = m['2']['17']
            s.add_exp = 0
            s.training_status = 'done' if '15' in m['2'] else 'not_doing'
            s.duplicate_count = 0
            s.illust = 'after_training' if '15' in m['2'] else 'normal'
            s.skill_exp = 0
            s.skill_level = 5

    d = o.user_deck_map.entries[1]
    d.deck_id = 1
    d.deck_name = '밴드1'
    d.leader = 1
    d.member1 = 13
    d.member2 = 17
    d.member3 = 9
    d.member4 = 5
    d.deck_type = 'normal'

    ss = []
    for m in _suite_master['21']['1']:  # MasterMainStoryMap
        s = user_story_pb2.UserMainStory()
        s.user_id = user_id
        s.story_id = m['1']
        s.status = 'already_read'
        ss.append(s)
    o.user_main_story_list.entries.extend(
        sorted(ss, key=attrgetter('story_id'), reverse=True))

    for i in range(1, 10):
        b = o.user_bonds_list.entries.add()
        b.user_id = user_id
        b.bonds_id = i
        b.level = 1
        b.bonds = (i+1) * 5

    for i in [1, 2, 3, 4, 5, 18, 21]:
        r = o.user_band_rank_map.entries[i]
        r.user_id = user_id
        r.band_id = i
        r.band_rank = 1
        r.exp = 0
        r.add_exp = 0
        r.pooled_exp = 0
        r.total_exp = 0
        r.next_exp = 400

    def build_band_story_list_from_master(field_number):
        ss = []
        for m in _suite_master[str(field_number)]['1']:
            s = user_band_story_pb2.UserBandStory()
            s.user_id = user_id
            s.band_story_id = m['1']
            s.band_id = m['2']['2']
            s.status = 'already_read'
            s.seq = m['2']['3']
            ss.append(s)
        return sorted(ss, key=attrgetter('seq'), reverse=True)

    o.user_poppin_party_story_list.entries.extend(
        build_band_story_list_from_master(22))  # masterPoppinPartyStoryMap

    o.user_afterglow_story_list.entries.extend(
        build_band_story_list_from_master(23))  # masterAfterglowStoryMap

    o.user_pastel_palettes_story_list.entries.extend(
        build_band_story_list_from_master(24))  # masterPastelPalettesStoryMap

    o.user_hello_happy_world_story_list.entries.extend(
        build_band_story_list_from_master(25))  # masterHelloHappyWorldStoryMap

    o.user_roselia_story_list.entries.extend(
        build_band_story_list_from_master(26))  # masterRoseliaStoryMap

    ls = o.user_commons_live2d_map.entries['event_box_gacha_top_first'].entries
    l = ls.add()
    l.live2d_id = 3131
    l.live2d_category = 'event_box_gacha_top_first'
    ls = o.user_commons_live2d_map.entries['live_menu'].entries
    for i in [10, 11, 12,
              22, 23, 24,
              34, 35, 36,
              46, 47, 48,
              58, 59, 60,
              7217, 7218, 7219,     # Related to seasons
              7251, 7252, 7253,
              7285, 7286, 7287,
              7319, 7320, 7321,
              7352, 7353, 7354]:
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'live_menu'
    ls = o.user_commons_live2d_map.entries['mission'].entries
    for i in range(3126, 3131):
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'mission'
    ls = o.user_commons_live2d_map.entries['login_bonus'].entries
    for i in [7, 8, 9,
              19, 20, 21,
              31, 32, 33,
              43, 44, 45,
              55, 56, 57,
              9557, 9558, 9559,     # Related to seasons
              9591, 9592, 9593,
              9625, 9626, 9627,
              9659, 9660, 9661,
              9692, 9693, 9694]:
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'login_bonus'
    ls = o.user_commons_live2d_map.entries['story_menu'].entries
    for i in [1, 2, 3,
              14, 15,
              25, 26, 27,
              37, 38, 39,
              49, 50, 51,
              8387, 8388, 8389,     # Related to seasons
              8421, 8422, 8423,
              8455, 8456, 8457,
              8489, 8490, 8491,
              8522, 8523, 8524]:
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'story_menu'
    ls = o.user_commons_live2d_map.entries['event_box_gacha_top'].entries
    for i in range(3132, 3135):
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'event_box_gacha_top'
    ls = o.user_commons_live2d_map.entries['event_box_gacha_after'].entries
    for i in range(3142, 3145):
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'event_box_gacha_after'
    ls = o.user_commons_live2d_map.entries['band_menu'].entries
    for i in [4, 5, 6,
              16, 17, 18,
              28, 29, 30,
              40, 41, 42,
              52, 53, 54,
              6047, 6048, 6049,     # Related to seasons
              6081, 6082, 6083,
              6115, 6116, 6117,
              6149, 6150, 6151,
              6182, 6183, 6184]:
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'band_menu'
    ls = o.user_commons_live2d_map.entries['birthday_page'].entries
    for i in [10711, 10712, 10713,
              10745, 10746, 10747,
              10779, 10780, 10781,
              10782, 10783, 10784,
              10813, 10814, 10815,
              10847, 10848, 10849,
              10862, 10863, 10864]:
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'birthday_page'
    ls = o.user_commons_live2d_map.entries['event_box_gacha_before'].entries
    for i in range(3136, 3139):
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'event_box_gacha_before'
    ls = o.user_commons_live2d_map.entries['event_box_gacha_after_win'].entries
    for i in range(3140, 3142):
        l = ls.add()
        l.live2d_id = i
        l.live2d_category = 'event_box_gacha_after_win'

    for m in _suite_master['4']['1']:   # masterCharacterSituationMap
        if '14' not in m['2']:
            continue
        for me in m['2']['14']['1']:    # episodes
            e = o.user_episode_map.entries[me['1']]
            e.user_id = user_id
            e.episode_id = me['1']
            e.episode_status = 'already_read'

    for m in _suite_master['1']['1']:   # MasterMusicListGetResponse
        i = o.user_music_inventory_list.entries.add()
        i.user_id = user_id
        i.music_id = m['1']
        i.seq = 1
        i.has_mv = m['1'] in (
            v['1'] for v in _suite_master['109']['1']
        )   # MasterMusicVideoListMap
        i.is_favorite = False

    for m in _suite_master['31']['1']:  # MasterCostumeMap
        c = o.user_costume_map.entries[m['1']]
        c.user_id = user_id
        c.costume_id = m['1']

    for i in [4, 5, 6,
              11, 12, 13,
              18, 19, 20,
              25, 26, 27,
              32, 33, 34,
              39, 40, 41,
              46, 47, 48,
              53, 54, 55,
              61, 62,
              67, 68, 69]:
        t = o.user_after_live_talk_list_map.entries['success'].entries.add()
        t.after_live_talk_id = i
        t.after_live_talk_type = 'success'
    for i in [7, 14, 21, 28, 35,
              42, 49, 56, 63, 70]:
        t = o.user_after_live_talk_list_map.entries['failure'].entries.add()
        t.after_live_talk_id = i
        t.after_live_talk_type = 'failure'
    for i in [1, 2, 3,
              8, 9, 10,
              15, 16, 17,
              22, 23, 24,
              29, 30, 31,
              36, 37, 38,
              43, 44, 45,
              50, 51, 52,
              57, 58, 59,
              64, 65, 66]:
        t = (o.user_after_live_talk_list_map.entries['great_success'].entries
             .add())
        t.after_live_talk_id = i
        t.after_live_talk_type = 'great_success'

    for i, c in [(1, 1), (26, 6), (51, 11), (76, 16), (101, 21)]:
        a = o.user_area_item_map.entries[i]
        a.user_id = user_id
        a.area_item_id = i
        a.area_item_category = c
        a.level = 1

    o.user_resource_count.present = 0

    b = o.user_live_boost
    b.user_id = user_id
    b.live_boost = 10
    b.server_date = int(time.time()*1000)
    b.live_boost_bonus_type = 'default'

    for i in range(1, 20):
        s = o.user_area_status_map.entries[i]
        s.user_id = user_id
        s.area_id = i

    b = o.user_login_bonus_map.entries[1]
    b.user_id = user_id
    b.login_bonus_id = 1
    b.days = 5

    b = o.user_home_banner_list.entries.add()
    b.home_banner_id = 1283
    b = o.user_home_banner_list.entries.add()
    b.home_banner_id = 1437
    b = o.user_home_banner_list.entries.add()
    b.home_banner_id = 1480
    b = o.user_home_banner_list.entries.add()
    b.home_banner_id = 1482

    for m in _suite_master['46']['1']:  # MasterStampMap
        s = o.user_stamp_map.entries[m['1']]
        s.user_id = user_id
        s.stamp_id = m['1']
        s.seq = m['2']['2']

    for i in [100, 101, 102, 103, 104, 105, 111, 112]:
        d = o.user_degree_map.entries[i]
        d.user_id = user_id
        d.degree_id = i

    for c, ls in [
            (1, [1, 2, 3, 4, 5,
                 4374, 4375, 4376,
                 9000, 9001, 9002]),
            (2, [6, 7, 8, 9, 10,
                 4408, 4409, 4410,
                 9003, 9004, 9005]),
            (3, [11, 12, 13, 14, 15,
                 4442, 4443, 4444,
                 9006, 9007, 9008]),
            (4, [16, 17, 18, 19, 20,
                 4476, 4477, 4478,
                 9009, 9010, 9011]),
            (5, [21, 22, 23, 24, 25,
                 4509, 4510, 4511,
                 9012, 9013, 9014]),
            (6, [26, 27, 28, 29, 30,
                 4542, 4543, 4544,
                 9015, 9016, 9017]),
            (7, [31, 32, 33, 34, 35,
                 4575, 4576, 4577,
                 9018, 9019, 9020]),
            (8, [36, 37, 38, 39, 40,
                 4608, 4609, 4610,
                 9021, 9022, 9023]),
            (9, [41, 42, 43, 44, 45,
                 4641, 4642, 4643,
                 9024, 9025, 9026]),
            (10, [46, 47, 48, 49, 50,
                  4674, 4675, 4676,
                  9027, 9028, 9029]),
            (11, [51, 52, 53, 54, 55,
                  5209, 5210, 5211,
                  9030, 9031, 9032]),
            (12, [56, 57, 58, 59, 60,
                  5243, 5244, 5245,
                  9033, 9034, 9035]),
            (13, [61, 62, 63, 64, 65,
                  5277, 5278, 5279,
                  9036, 9037, 9038]),
            (14, [66, 67, 68, 69, 70,
                  5310, 5311, 5312,
                  9039, 9040, 9041]),
            (15, [71, 72, 73, 74, 75,
                  5343, 5344, 5345,
                  9042, 9043, 9044]),
            (16, [76, 77, 78, 79, 80,
                  5038, 5039, 5040,
                  9045, 9046, 9047]),
            (17, [81, 82, 83, 84, 85,
                  5073, 5074, 5075,
                  9048, 9049, 9050]),
            (18, [86, 87, 88, 89, 90,
                  5107, 5108, 5109,
                  9051, 9052, 9053]),
            (19, [91, 92, 94, 95,
                  5142, 5143, 5144,
                  9054, 9055, 9056]),
            (20, [96, 97, 98, 99, 100,
                  5176, 5177, 5178,
                  9057, 9058, 9059]),
            (21, [101, 103, 104, 105,
                  4707, 4708, 4709,
                  9060, 9061, 9062]),
            (22, [106, 107, 108, 109, 110,
                  4740, 4741, 4742,
                  9063, 9064, 9065]),
            (23, [111, 112, 114, 115,
                  4774, 4775, 4776,
                  9066, 9067, 9068]),
            (24, [116, 117, 118, 119, 120,
                  4807, 4808, 4809,
                  9069, 9070, 9071]),
            (25, [121, 123, 124, 125,
                  4840, 4841, 4842,
                  9072, 9073, 9074]),
            (26, [3755, 3756, 3757, 3758, 3759,
                  3920, 3921, 3922,
                  5377, 5378, 5379]),
            (27, [3760, 3761, 3762, 3763, 3764,
                  3923, 3924, 3925,
                  5410, 5411, 5412]),
            (28, [3765, 3766, 3767, 3768, 3769,
                  3926, 3927, 3928,
                  5443, 5444, 5445]),
            (29, [3770, 3771, 3772, 3773, 3774,
                  3929, 3930, 3931,
                  5476, 5477, 5478]),
            (30, [3775, 3776, 3777, 3778, 3779,
                  3932, 3933, 3934,
                  5509, 5510, 5511]),
            (31, [3935, 3936, 3937, 3938, 3939,
                  4083, 4084, 4085,
                  4873, 4874, 4875]),
            (32, [3965, 3966, 3967, 3968, 3969,
                  4086, 4087, 4088,
                  4906, 4907, 4908]),
            (33, [3994, 3995, 3996, 3997, 3998,
                  4089, 4090, 4091,
                  4939, 4940, 4941]),
            (34, [4024, 4025, 4026, 4027, 4028,
                  4092, 4093, 4094,
                  4972, 4973, 4974]),
            (35, [4054, 4055, 4056, 4057, 4058,
                  4095, 4096, 4097,
                  5005, 5006, 5007])
    ]:
        for l in ls:
            e = o.user_character_profile_live2d_map.entries[c].entries.add()
            e.character_id = c
            e.live2d_id = l

    for g, is_ in [
            (101, [2, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]),
            (201, range(1001, 1031)),
    ]:
        for i in is_:
            m = o.user_mission_map.entries[i].entries.add()
            m.user_id = user_id
            m.mission_id = i
            m.seq = 1
            m.progress = 1
            m.mission_progress_type = 'in_progress'
            m.mission_group_id = g
    m = o.user_mission_map.entries[29].entries[0].progress = 187989
    m = o.user_mission_map.entries[30].entries[0].progress = 146467
    m = o.user_mission_map.entries[31].entries[0].progress = 139446
    m = o.user_mission_map.entries[32].entries[0].progress = 136045
    m = o.user_mission_map.entries[33].entries[0].progress = 142245
    m = o.user_mission_map.entries[34].entries[0].progress = 149055
    for i in range(1001, 1006):
        m = o.user_mission_map.entries[i].entries[0].progress = 2
    o.user_mission_map.limited_last_updated_at = int(time.time()*1000)

    s = o.user_generic_story_map.entries[34]
    s.user_id = user_id
    s.generic_story_id = 34
    s.status = 'unread'

    o.user_season.season_id = 27

    with open('krdori/responses/user_event_story_memorial_response.binpb',
               'rb') as f:
        m = (user_event_story_memorial_pb2.UserEventStoryMemorialResponse
             .FromString(f.read()))
        for k, v in m.past_event_story_map.entries.items():
            sm = o.user_event_story_memorial_map.entries[k]
            sm.event_id = k
            for e in v.entries:
                s = sm.user_event_story_list.entries.add()
                s.user_id = user_id
                s.event_id = k
                s.seq = e.seq
                s.status = 'already_read'
            sm.is_exist_un_read_story = False
            sm.is_locked = False

    o.user_released_bonds_id_list.entries.extend(range(1, 66))
    o.user_released_bonds_id_list.entries.extend(range(148, 158))
    o.user_released_bonds_id_list.entries.extend(range(169, 179))
    o.user_released_bonds_id_list.entries.extend(range(180, 197))

    t = o.user_miracle_ticket_map.entries[4]
    t.user_id = user_id
    t.miracle_ticket_id = 4
    t.quantity = 1
    t.exchange_end_at = (int(time.time())+86400*30) * 1000

    for m in _suite_master['30']['1']:  # MasterMusicShopMap
        s = o.user_music_shop_map.entries[m['2']['2']].entries.add()
        s.user_id = user_id
        s.music_shop_id = m['1']
        s.shop_id = m['2']['2']
        s.shop_category = m['2']['3']
        s.music_id = m['2']['5']
        s.status = 'sold_out'
        s.seq = m['2']['4']

    for m in _suite_master['96']['1']:  # MasterBackstageTalkSetMap
        o.user_backstage_talk_set_read_history_map.entries[m['1']] = (
            'already_read')

    o.user_friend_relation_detail.application_limit = 50
    o.user_friend_relation_detail.approval_limit = 50
    o.user_friend_relation_detail.friend_limit = 50

    d = o.user_profile_degree_map.entries['first']
    d.user_id = user_id
    d.profile_degree_type = 'first'
    d.degree_id = 100

    i = o.user_deco_frame_inventory_map.entries[1]
    i.user_id = user_id
    i.deco_frame_id = 1
    i.level = 1

    for i in [310, 320, 330, 340, 350]:
        p = o.user_deco_pins_inventory_map.entries[i]
        p.user_id = user_id
        p.deco_pins_id = i
        p.quantity = 1

    o.user_deco_equipment.user_id = user_id
    o.user_deco_equipment.deco_frame_id = 1

    for m in _suite_master['109']['1']:     # MasterMusicVideoListMap
        if isinstance(m['2']['1'], list):
            for v in m['2']['1']:
                i = (o.user_music_video_list_map
                     .user_music_video_inventory_list_map.entries[m['1']]
                     .entries.add())
                i.user_id = user_id
                i.music_id = m['1']
                i.seq = v['6']
        else:
            i = (o.user_music_video_list_map
                 .user_music_video_inventory_list_map.entries[m['1']]
                 .entries.add())
            i.user_id = user_id
            i.music_id = m['1']
            i.seq = m['2']['1']['6']

    o.user_event_box_gacha_spin_settings.lump_spin_flg = False
    o.user_event_box_gacha_spin_settings.auto_stop_flg = False

    o.user_morfonica_story_list.entries.extend(
        build_band_story_list_from_master(401))     # masterMorfonicaStoryMap

    o.user_raise_a_suilen_story_list.entries.extend(
        build_band_story_list_from_master(402))     # masterRaiseASuilenStoryMap

    o.user_comeback_status.comeback_gacha_id = 0

    for i in [1, 2, 7, 8, 10, 11, 13, 14, 16, 17]:
        s = o.user_digest_story_list.entries.add()
        s.user_id = user_id
        s.digest_story_id = i
        s.status = 'unread'

    o.user_receivable_present_location_list.location_list.append(
        'countdown_page')

    d = o.user_deck_list.entries.add()
    d.deck_id = 1
    d.deck_name = '밴드1'
    d.leader = 1
    d.member1 = 13
    d.member2 = 17
    d.member3 = 9
    d.member4 = 5
    d.deck_type = 'normal'

    # TODO: user_gallery_list

    for i, as_ in [
        (1, [('powerful', 9, 1430, 0, 37642),
             ('happy', 1428, 17, 0, 41546),
             ('pure', 1, 1431, 0, 37793),
             ('cool', 1427, 1429, 5, 71008)]),
        (2, [('powerful', 1432, 0, 0, 27494),
             ('happy', 1433, 0, 0, 33697),
             ('pure', 1436, 1434, 0, 57784),
             ('cool', 1435, 0, 0, 27492)]),
        (3, [('powerful', 1439, 1438, 0, 50766),
             ('happy', 1437, 0, 0, 33694),
             ('pure', 1441, 0, 0, 24089),
             ('cool', 1440, 0, 0, 33696)]),
        (4, [('powerful', 1444, 1445, 0, 51582),
             ('happy', 1446, 0, 0, 26679),
             ('pure', 1442, 0, 0, 33694),
             ('cool', 1443, 0, 0, 27491)]),
        (5, [('powerful', 1448, 0, 0, 33697),
             ('happy', 1451, 0, 0, 26677),
             ('pure', 1450, 1447, 0, 48179),
             ('cool', 1449, 0, 0, 27492)]),
        (21, [('powerful', 1453, 0, 0, 33697),
              ('happy', 1454, 0, 0, 27491),
              ('pure', 1456, 0, 0, 26676),
              ('cool', 1455, 1452, 0, 61191)])
    ]:
        b = o.user_band_deck_rating_map.entries[i]
        for a, l, m1, m2, s in as_:
            d = b.deck_rating.add()
            d.attribute = a
            d.leader = l
            if m1:
                d.member1 = m1
            if m2:
                d.member2 = m2
            d.rank = 'c'
            d.score = s
            d.level = 0
            d.lower_rating = 1
            d.upper_rating = 400_000
        t = b.total_rating
        t.rank = 'c'
        t.score = sum(a[4] for a in as_)
        t.level = 0
        t.lower_rating = 1
        t.upper_rating = 1_600_000

    o.user_auto_live.daily_auto_live_use_count = 0
    o.user_auto_live.reset_time = int(time.time()*1000)

    o.user_monthly_mission.mission_season_id = 0
    o.user_monthly_mission.live_point = 0
    o.user_monthly_mission.is_purchase_premium_mission_pass = False

    # with open('suite_user_get_response.txtpb', 'w', encoding='utf-8') as f:
    #     f.write(str(o))
    _suite_user = o
    return o.SerializeToString()


@app.put('/api/suite/user/<int:user_id>/loginbonus/acceptall')
def suite_login_bonus_accept_all_api(user_id):
    o = suite_user_login_bonus_pb2.SuiteUserLoginBonusAcceptAllResponse()
    u = o.update_resources

    u.user_resource_count.present = 1

    b = u.user_live_boost
    b.user_id = user_id
    b.live_boost = 10
    b.server_date = int(time.time()*1000)
    b.live_boost_bonus_type = 'default'

    t = u.user_miracle_ticket_map.entries[4]
    t.user_id = user_id
    t.miracle_ticket_id = 4
    t.quantity = 1
    t.exchange_end_at = (int(time.time())+86400*30) * 1000

    return o.SerializeToString()


@app.get('/api/system/application')
def get_server_system_api():
    o = server_system_pb2.ServerSystem()
    o.server_date = int(time.time()*1000)
    o.time_zone_raw_offset = 32_400_000
    return o.SerializeToString()


@app.get('/api/cleanupinfo')
def get_cleanup_info_api():
    with open('krdori/responses/cleanup_info.binpb', 'rb') as f:
        o = f.read()
    return o


@app.get('/api/suite/user/<int:user_id>/area')
def get_user_area_character_api(user_id):
    with open('krdori/responses/user_area.binpb', 'rb') as f:
        o = user_area_pb2.UserArea.FromString(f.read())
    o.user_season.season_id = 27
    return o.SerializeToString()


@app.put('/api/suite/user/<int:user_id>/loginbonus/<int:login_bonus_id>/watch')
def suite_login_bonus_api(user_id, login_bonus_id):
    o = suite_user_login_bonus_pb2.SuiteUserLoginBonus()

    b = o.update_resources.user_live_boost
    b.user_id = user_id
    b.live_boost = 10
    b.server_date = int(time.time()*1000)
    b.live_boost_bonus_type = 'default'

    o.update_resources.user_login_bonus_map.SetInParent()

    r = o.accept_response.player_resources.entries.add()
    r.resource_id = 1
    r.resource_type = 'practice_ticket'
    r.quantity = 5
    r.lb_bonus = 1

    return o.SerializeToString()


@app.get('/api/user/<int:user_id>/bandstory/<int:band_id>')
def user_band_story_api(user_id, band_id):
    o = user_band_story_pb2.UserBandStoryList()
    if band_id == 1:
        o.CopyFrom(_suite_user.user_poppin_party_story_list)
    elif band_id == 2:
        o.CopyFrom(_suite_user.user_afterglow_story_list)
    elif band_id == 3:
        o.CopyFrom(_suite_user.user_hello_happy_world_story_list)
    elif band_id == 4:
        o.CopyFrom(_suite_user.user_pastel_palettes_story_list)
    elif band_id == 5:
        o.CopyFrom(_suite_user.user_roselia_story_list)
    elif band_id == 18:
        o.CopyFrom(_suite_user.user_raise_a_suilen_story_list)
    elif band_id == 21:
        o.CopyFrom(_suite_user.user_morfonica_story_list)
    return o.SerializeToString()


# @app.post('/api/suite/user/<int:user_id>/bandstory/<int:band_id>
#           '/id/<int:band_story_id>')
# def post_suite_user_band_story_api(user_id, band_id, band_story_id):
#     o = suite_user_story_pb2.SuiteUserBandStoryResponse()
#     o.SerializeToString()


@app.post('/api/user/<int:user_id>/logging/playstory')
def post_logging_play_story_api(user_id):
    return b''


@app.post('/api/user/<int:user_id>/musicvideo/watching/<int:music_id>'
          '/<int:seq>')
def post_music_video_watching_api(user_id, music_id, seq):
    return b''


@app.get('/api/user/<int:user_id>/actionset/album/<int:character_id>')
def get_user_action_set_album_api(user_id, character_id):
    o = user_action_set_album_pb2.UserActionSetAlbumMap()

    with open('krdori/responses/jp/7.0.0.110/master_action_set_map.json',
              'rb') as f:
        amap = json.loads(f.read())

    for m in _suite_master['14']['1']:  # MasterActionSetMap
        if m['1'] >= 90000:
            continue
        if (isinstance(m['2']['3'], list) and character_id in m['2']['3']
                or character_id == m['2']['3']):
            a = o.entries[m['1']]
            a.action_set_id = m['1']
            a.balloon_text = m['2']['11']
            a.is_memorial = (amap[str(m['1'])]['startSeason'] == 'season_1'
                             and 'endSeason' in amap[str(m['1'])])

    return o.SerializeToString()


@app.get('/api/user/<int:user_id>/backstagetalkset/readhistory')
def get_user_backstage_talk_set_read_history_map_api(user_id):
    o = user_backstage_talk_set_pb2.UserBackstageTalkSetReadHistoryMap()
    for m in _suite_master['96']['1']:  # MasterBackstageTalkSetMap
        o.entries[m['1']] = 'already_read'
    return o.SerializeToString()


@app.get('/api/user/<int:user_id>/memorialstory')
def get_user_memorial_story_api(user_id):
    with open('krdori/responses/user_event_story_memorial_response.binpb',
               'rb') as f:
        o = (user_event_story_memorial_pb2.UserEventStoryMemorialResponse
             .FromString(f.read()))

    o.ClearField('user_event_story_memorial_map')
    for k, v in o.past_event_story_map.entries.items():
        m = o.user_event_story_memorial_map.entries[k]
        m.event_id = k
        for e in v.entries:
            s = m.user_event_story_list.entries.add()
            s.user_id = user_id
            s.event_id = k
            s.seq = e.seq
            s.status = 'already_read'
        m.is_exist_un_read_story = False
        m.is_locked = False

    return o.SerializeToString()


@app.post('/api/suite/user/<int:user_id>/memorialstory/<int:event_id>'
          '/<int:seq>')
def post_user_memorial_story_api(user_id, event_id, seq):
    o = suite_user_event_story_memorial_pb2.SuiteReadStoryResponse()

    o.update_resources.user_event_story_memorial_map.CopyFrom(
        _suite_user.user_event_story_memorial_map)

    r = o.user_story_event_read_story_response
    s = r.read_user_event_story
    s.user_id = user_id
    s.event_id = event_id
    s.seq = seq
    s.status = 'already_read'

    r.rewards.SetInParent()
    r.newly_opened_contents.SetInParent()

    return o.SerializeToString()


@app.put('/api/suite/user/<int:user_id>/character/<int:character_id>'
            '/costume/<int:costume_id>')
def put_user_character_api(user_id, character_id, costume_id):
    o = suite_user_character_pb2.SuiteUserCharacter()

    c = o.user_character
    c.user_id = user_id
    c.character_id = character_id
    c.costume_id = costume_id

    return o.SerializeToString()


@app.delete('/api/suite/user/<int:user_id>/character/<int:character_id>'
            '/costume')
def delete_user_character_api(user_id, character_id):
    o = suite_user_character_pb2.SuiteUserCharacter()
    return o.SerializeToString()


# @app.post('/api/suite/user/<int:user_id>/mainstory/<int:main_story_id>')
# def post_user_main_story_api(user_id, main_story_id):
#     o = suite_user_story_pb2.SuiteUserMainStoryResponse()
#     o.update_resources.user_main_story_list.CopyFrom(
#         _suite_user.user_main_story_list)
#     o.user_main_story_list.CopyFrom(_suite_user.user_main_story_list)
#     o.rewards.SetInParent()
#     o.newly_opened_contents.SetInParent()
#     return o.SerializeToString()


def start(port):
    print(f'Running game server on port {port}...')
    app.run(host='0.0.0.0', port=port, debug=False)

