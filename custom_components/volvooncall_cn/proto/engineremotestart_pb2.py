# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: engineremotestart.proto
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
    'engineremotestart.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65ngineremotestart.proto\x12(services.vehiclestates.engineremotestart\"&\n\x17GetEngineRemoteStartReq\x12\x0b\n\x03vin\x18\x02 \x01(\t\"D\n\x1cGetEngineRemoteStartDataHead\x12\x12\n\nupdateTime\x18\x01 \x01(\x03\x12\x10\n\x08unknown1\x18\x02 \x01(\x03\"\xa1\x02\n\x18GetEngineRemoteStartData\x12T\n\x04head\x18\x01 \x01(\x0b\x32\x46.services.vehiclestates.engineremotestart.GetEngineRemoteStartDataHead\x12V\n\rengineStarted\x18\x02 \x01(\x0e\x32?.services.vehiclestates.engineremotestart.EngineRemoteStartType\x12W\n\x0e\x65ngineStarting\x18\x03 \x01(\x0e\x32?.services.vehiclestates.engineremotestart.EngineRemoteStartType\"y\n\x18GetEngineRemoteStartResp\x12\x0b\n\x03vin\x18\x02 \x01(\t\x12P\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x42.services.vehiclestates.engineremotestart.GetEngineRemoteStartData*C\n\x15\x45ngineRemoteStartType\x12\x0b\n\x07Unknow1\x10\x00\x12\x06\n\x02No\x10\x01\x12\x0c\n\x08Starting\x10\x02\x12\x07\n\x03Yes\x10\x03\x32\xbe\x01\n\x18\x45ngineRemoteStartService\x12\xa1\x01\n\x14GetEngineRemoteStart\x12\x41.services.vehiclestates.engineremotestart.GetEngineRemoteStartReq\x1a\x42.services.vehiclestates.engineremotestart.GetEngineRemoteStartResp\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'engineremotestart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENGINEREMOTESTARTTYPE']._serialized_start=594
  _globals['_ENGINEREMOTESTARTTYPE']._serialized_end=661
  _globals['_GETENGINEREMOTESTARTREQ']._serialized_start=69
  _globals['_GETENGINEREMOTESTARTREQ']._serialized_end=107
  _globals['_GETENGINEREMOTESTARTDATAHEAD']._serialized_start=109
  _globals['_GETENGINEREMOTESTARTDATAHEAD']._serialized_end=177
  _globals['_GETENGINEREMOTESTARTDATA']._serialized_start=180
  _globals['_GETENGINEREMOTESTARTDATA']._serialized_end=469
  _globals['_GETENGINEREMOTESTARTRESP']._serialized_start=471
  _globals['_GETENGINEREMOTESTARTRESP']._serialized_end=592
  _globals['_ENGINEREMOTESTARTSERVICE']._serialized_start=664
  _globals['_ENGINEREMOTESTARTSERVICE']._serialized_end=854
# @@protoc_insertion_point(module_scope)
