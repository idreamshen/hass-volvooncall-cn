# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dtlinternet.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'dtlinternet.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64tlinternet.proto\x12\x0b\x64tlinternet\"*\n\x1bStreamLastKnownLocationsReq\x12\x0b\n\x03vin\x18\x01 \x01(\t\";\n\x17otherLocationUnknowData\x12\x0f\n\x07unknow3\x18\x01 \x01(\x05\x12\x0f\n\x07unknow4\x18\x02 \x01(\x05\"l\n\x0eotherLocations\x12\x11\n\tlongitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x35\n\x07unknow2\x18\x03 \x01(\x0b\x32$.dtlinternet.otherLocationUnknowData\"\x8d\x01\n\x1cStreamLastKnownLocationsResp\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x0f\n\x07unknow1\x18\x04 \x01(\x05\x12*\n\x05other\x18\x05 \x01(\x0b\x32\x1b.dtlinternet.otherLocations2\x89\x01\n\x12\x44tlInternetService\x12s\n\x18StreamLastKnownLocations\x12(.dtlinternet.StreamLastKnownLocationsReq\x1a).dtlinternet.StreamLastKnownLocationsResp\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dtlinternet_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STREAMLASTKNOWNLOCATIONSREQ']._serialized_start=34
  _globals['_STREAMLASTKNOWNLOCATIONSREQ']._serialized_end=76
  _globals['_OTHERLOCATIONUNKNOWDATA']._serialized_start=78
  _globals['_OTHERLOCATIONUNKNOWDATA']._serialized_end=137
  _globals['_OTHERLOCATIONS']._serialized_start=139
  _globals['_OTHERLOCATIONS']._serialized_end=247
  _globals['_STREAMLASTKNOWNLOCATIONSRESP']._serialized_start=250
  _globals['_STREAMLASTKNOWNLOCATIONSRESP']._serialized_end=391
  _globals['_DTLINTERNETSERVICE']._serialized_start=394
  _globals['_DTLINTERNETSERVICE']._serialized_end=531
# @@protoc_insertion_point(module_scope)
