# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csystem.proto\"\x18\n\x04item\x12\x10\n\x08itemName\x18\x01 \x01(\t\"6\n\x03\x62id\x12\x10\n\x08itemName\x18\x01 \x01(\t\x12\x0e\n\x06\x62idder\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x05\"\x16\n\x06result\x12\x0c\n\x04text\x18\x01 \x01(\t\"#\n\nsystemList\x12\x15\n\x07\x62idlist\x18\x01 \x03(\x0b\x32\x04.bid2[\n\x06System\x12\x1a\n\x06\x64oList\x12\x05.item\x1a\x07.result\"\x00\x12\x18\n\x05\x64oBid\x12\x04.bid\x1a\x07.result\"\x00\x12\x1b\n\x07\x64oQuery\x12\x05.item\x1a\x07.result\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'system_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ITEM._serialized_start=16
  _ITEM._serialized_end=40
  _BID._serialized_start=42
  _BID._serialized_end=96
  _RESULT._serialized_start=98
  _RESULT._serialized_end=120
  _SYSTEMLIST._serialized_start=122
  _SYSTEMLIST._serialized_end=157
  _SYSTEM._serialized_start=159
  _SYSTEM._serialized_end=250
# @@protoc_insertion_point(module_scope)
