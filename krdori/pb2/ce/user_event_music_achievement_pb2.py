# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_event_music_achievement.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0krdori/pb2/ce/user_event_music_achievement.proto\x12\rkrdori.pb2.ce\"}\n\x19UserEventMusicAchievement\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\r\x12\x10\n\x08music_id\x18\x03 \x01(\r\x12\x18\n\x10\x61\x63hievement_type\x18\x04 \x01(\t\x12\x11\n\tlive_type\x18\x05 \x01(\t\"Z\n\x1dUserEventMusicAchievementList\x12\x39\n\x07\x65ntries\x18\x01 \x03(\x0b\x32(.krdori.pb2.ce.UserEventMusicAchievement\"\xc9\x01\n\x1dUserEventMusicAchievementsMap\x12J\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x39.krdori.pb2.ce.UserEventMusicAchievementsMap.EntriesEntry\x1a\\\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.krdori.pb2.ce.UserEventMusicAchievementList:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_event_music_achievement_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USEREVENTMUSICACHIEVEMENTSMAP_ENTRIESENTRY._options = None
  _USEREVENTMUSICACHIEVEMENTSMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USEREVENTMUSICACHIEVEMENT']._serialized_start=67
  _globals['_USEREVENTMUSICACHIEVEMENT']._serialized_end=192
  _globals['_USEREVENTMUSICACHIEVEMENTLIST']._serialized_start=194
  _globals['_USEREVENTMUSICACHIEVEMENTLIST']._serialized_end=284
  _globals['_USEREVENTMUSICACHIEVEMENTSMAP']._serialized_start=287
  _globals['_USEREVENTMUSICACHIEVEMENTSMAP']._serialized_end=488
  _globals['_USEREVENTMUSICACHIEVEMENTSMAP_ENTRIESENTRY']._serialized_start=396
  _globals['_USEREVENTMUSICACHIEVEMENTSMAP_ENTRIESENTRY']._serialized_end=488
# @@protoc_insertion_point(module_scope)