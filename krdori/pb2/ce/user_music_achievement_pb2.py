# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_music_achievement.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*krdori/pb2/ce/user_music_achievement.proto\x12\rkrdori.pb2.ce\"S\n\x14UserMusicAchievement\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08music_id\x18\x02 \x01(\r\x12\x18\n\x10\x61\x63hievement_type\x18\x03 \x01(\t\"P\n\x18UserMusicAchievementList\x12\x34\n\x07\x65ntries\x18\x01 \x03(\x0b\x32#.krdori.pb2.ce.UserMusicAchievement\"\xb8\x01\n\x17UserMusicAchievementMap\x12\x44\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x33.krdori.pb2.ce.UserMusicAchievementMap.EntriesEntry\x1aW\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.krdori.pb2.ce.UserMusicAchievementList:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_music_achievement_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USERMUSICACHIEVEMENTMAP_ENTRIESENTRY._options = None
  _USERMUSICACHIEVEMENTMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USERMUSICACHIEVEMENT']._serialized_start=61
  _globals['_USERMUSICACHIEVEMENT']._serialized_end=144
  _globals['_USERMUSICACHIEVEMENTLIST']._serialized_start=146
  _globals['_USERMUSICACHIEVEMENTLIST']._serialized_end=226
  _globals['_USERMUSICACHIEVEMENTMAP']._serialized_start=229
  _globals['_USERMUSICACHIEVEMENTMAP']._serialized_end=413
  _globals['_USERMUSICACHIEVEMENTMAP_ENTRIESENTRY']._serialized_start=326
  _globals['_USERMUSICACHIEVEMENTMAP_ENTRIESENTRY']._serialized_end=413
# @@protoc_insertion_point(module_scope)