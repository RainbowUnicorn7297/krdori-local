# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_generic_story.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&krdori/pb2/ce/user_generic_story.proto\x12\rkrdori.pb2.ce\"M\n\x10UserGenericStory\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x18\n\x10generic_story_id\x18\x02 \x01(\r\x12\x0e\n\x06status\x18\x03 \x01(\t\"\xa8\x01\n\x13UserGenericStoryMap\x12@\n\x07\x65ntries\x18\x01 \x03(\x0b\x32/.krdori.pb2.ce.UserGenericStoryMap.EntriesEntry\x1aO\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.krdori.pb2.ce.UserGenericStory:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_generic_story_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USERGENERICSTORYMAP_ENTRIESENTRY._options = None
  _USERGENERICSTORYMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USERGENERICSTORY']._serialized_start=57
  _globals['_USERGENERICSTORY']._serialized_end=134
  _globals['_USERGENERICSTORYMAP']._serialized_start=137
  _globals['_USERGENERICSTORYMAP']._serialized_end=305
  _globals['_USERGENERICSTORYMAP_ENTRIESENTRY']._serialized_start=226
  _globals['_USERGENERICSTORYMAP_ENTRIESENTRY']._serialized_end=305
# @@protoc_insertion_point(module_scope)
