# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: krdori/pb2/ce/user_append_parameter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)krdori/pb2/ce/user_append_parameter.proto\x12\rkrdori.pb2.ce\"t\n\x13UserAppendParameter\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x14\n\x0csituation_id\x18\x02 \x01(\r\x12\x13\n\x0bperformance\x18\x03 \x01(\r\x12\x11\n\ttechnique\x18\x04 \x01(\r\x12\x0e\n\x06visual\x18\x05 \x01(\r\"\xb1\x01\n\x16UserAppendParameterMap\x12\x43\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x32.krdori.pb2.ce.UserAppendParameterMap.EntriesEntry\x1aR\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".krdori.pb2.ce.UserAppendParameter:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'krdori.pb2.ce.user_append_parameter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _USERAPPENDPARAMETERMAP_ENTRIESENTRY._options = None
  _USERAPPENDPARAMETERMAP_ENTRIESENTRY._serialized_options = b'8\001'
  _globals['_USERAPPENDPARAMETER']._serialized_start=60
  _globals['_USERAPPENDPARAMETER']._serialized_end=176
  _globals['_USERAPPENDPARAMETERMAP']._serialized_start=179
  _globals['_USERAPPENDPARAMETERMAP']._serialized_end=356
  _globals['_USERAPPENDPARAMETERMAP_ENTRIESENTRY']._serialized_start=274
  _globals['_USERAPPENDPARAMETERMAP_ENTRIESENTRY']._serialized_end=356
# @@protoc_insertion_point(module_scope)