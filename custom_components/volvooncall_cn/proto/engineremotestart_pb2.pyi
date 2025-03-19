from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EngineRemoteStartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknow1: _ClassVar[EngineRemoteStartType]
    No: _ClassVar[EngineRemoteStartType]
    Starting: _ClassVar[EngineRemoteStartType]
    Yes: _ClassVar[EngineRemoteStartType]
Unknow1: EngineRemoteStartType
No: EngineRemoteStartType
Starting: EngineRemoteStartType
Yes: EngineRemoteStartType

class GetEngineRemoteStartReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class GetEngineRemoteStartDataHead(_message.Message):
    __slots__ = ("updateTime", "unknown1")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    updateTime: int
    unknown1: int
    def __init__(self, updateTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class GetEngineRemoteStartData(_message.Message):
    __slots__ = ("head", "engineStarted", "engineStarting")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ENGINESTARTED_FIELD_NUMBER: _ClassVar[int]
    ENGINESTARTING_FIELD_NUMBER: _ClassVar[int]
    head: GetEngineRemoteStartDataHead
    engineStarted: EngineRemoteStartType
    engineStarting: EngineRemoteStartType
    def __init__(self, head: _Optional[_Union[GetEngineRemoteStartDataHead, _Mapping]] = ..., engineStarted: _Optional[_Union[EngineRemoteStartType, str]] = ..., engineStarting: _Optional[_Union[EngineRemoteStartType, str]] = ...) -> None: ...

class GetEngineRemoteStartResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: GetEngineRemoteStartData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[GetEngineRemoteStartData, _Mapping]] = ...) -> None: ...
