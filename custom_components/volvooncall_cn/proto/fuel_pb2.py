# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: fuel.proto
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
    'fuel.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nfuel.proto\x12\x1bservices.vehiclestates.fuel\"\x19\n\nGetFuelReq\x12\x0b\n\x03vin\x18\x02 \x01(\t\"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\x12\r\n\x05nanos\x18\x02 \x01(\x05\"\xc5\x01\n\x08\x46uelData\x12:\n\nupdateTime\x18\x01 \x01(\x0b\x32&.services.vehiclestates.fuel.Timestamp\x12\x19\n\x11\x64istanceToEmptyKm\x18\x02 \x01(\x05\x12\x17\n\x0fTMFuelAvgConsum\x18\x03 \x01(\x01\x12\x12\n\nfuelAmount\x18\x04 \x01(\x02\x12\x1c\n\x14\x64istanceToEmptyMiles\x18\x05 \x01(\x05\x12\x17\n\x0f\x41TFuleAvgConsum\x18\x06 \x01(\x01\"O\n\x0bGetFuelResp\x12\x0b\n\x03vin\x18\x02 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32%.services.vehiclestates.fuel.FuelData2o\n\x0b\x46uelService\x12`\n\x07GetFuel\x12\'.services.vehiclestates.fuel.GetFuelReq\x1a(.services.vehiclestates.fuel.GetFuelResp\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fuel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETFUELREQ']._serialized_start=43
  _globals['_GETFUELREQ']._serialized_end=68
  _globals['_TIMESTAMP']._serialized_start=70
  _globals['_TIMESTAMP']._serialized_end=113
  _globals['_FUELDATA']._serialized_start=116
  _globals['_FUELDATA']._serialized_end=313
  _globals['_GETFUELRESP']._serialized_start=315
  _globals['_GETFUELRESP']._serialized_end=394
  _globals['_FUELSERVICE']._serialized_start=396
  _globals['_FUELSERVICE']._serialized_end=507
# @@protoc_insertion_point(module_scope)
