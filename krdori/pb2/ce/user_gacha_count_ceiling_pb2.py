# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_gacha_count_ceiling.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,krdori/pb2/ce/user_gacha_count_ceiling.proto\x12\rkrdori.pb2.ce\"\xd6\x01\n\x15UserGachaCountCeiling\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08gacha_id\x18\x02 \x01(\r\x12\x13\n\x0btotal_count\x18\x03 \x01(\r\x12\x12\n\ngacha_seal\x18\x04 \x01(\r\x12-\n%is_inherit_gacha_seal_different_gacha\x18\x05 \x01(\x08\x12 \n\x18is_expired_exchange_item\x18\x06 \x01(\x08\x12 \n\x18\x65xchange_star_seal_count\x18\x07 \x01(\r\"\xb7\x01\n\x18UserGachaCountCeilingMap\x12\x45\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x34.krdori.pb2.ce.UserGachaCountCeilingMap.EntriesEntry\x1aT\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.krdori.pb2.ce.UserGachaCountCeiling:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_gacha_count_ceiling_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USERGACHACOUNTCEILINGMAP_ENTRIESENTRY._options = None
  _USERGACHACOUNTCEILINGMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USERGACHACOUNTCEILING']._serialized_start=64
  _globals['_USERGACHACOUNTCEILING']._serialized_end=278
  _globals['_USERGACHACOUNTCEILINGMAP']._serialized_start=281
  _globals['_USERGACHACOUNTCEILINGMAP']._serialized_end=464
  _globals['_USERGACHACOUNTCEILINGMAP_ENTRIESENTRY']._serialized_start=380
  _globals['_USERGACHACOUNTCEILINGMAP_ENTRIESENTRY']._serialized_end=464
# @@protoc_insertion_point(module_scope)