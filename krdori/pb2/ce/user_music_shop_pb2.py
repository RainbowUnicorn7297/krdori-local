# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_music_shop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#krdori/pb2/ce/user_music_shop.proto\x12\rkrdori.pb2.ce\"\x8e\x01\n\rUserMusicShop\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x15\n\rmusic_shop_id\x18\x02 \x01(\r\x12\x0f\n\x07shop_id\x18\x03 \x01(\r\x12\x15\n\rshop_category\x18\x04 \x01(\t\x12\x10\n\x08music_id\x18\x05 \x01(\r\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x0b\n\x03seq\x18\x07 \x01(\r\"B\n\x11UserMusicShopList\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.krdori.pb2.ce.UserMusicShop\"\xa3\x01\n\x10UserMusicShopMap\x12=\n\x07\x65ntries\x18\x01 \x03(\x0b\x32,.krdori.pb2.ce.UserMusicShopMap.EntriesEntry\x1aP\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .krdori.pb2.ce.UserMusicShopList:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_music_shop_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USERMUSICSHOPMAP_ENTRIESENTRY._options = None
  _USERMUSICSHOPMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USERMUSICSHOP']._serialized_start=55
  _globals['_USERMUSICSHOP']._serialized_end=197
  _globals['_USERMUSICSHOPLIST']._serialized_start=199
  _globals['_USERMUSICSHOPLIST']._serialized_end=265
  _globals['_USERMUSICSHOPMAP']._serialized_start=268
  _globals['_USERMUSICSHOPMAP']._serialized_end=431
  _globals['_USERMUSICSHOPMAP_ENTRIESENTRY']._serialized_start=351
  _globals['_USERMUSICSHOPMAP_ENTRIESENTRY']._serialized_end=431
# @@protoc_insertion_point(module_scope)