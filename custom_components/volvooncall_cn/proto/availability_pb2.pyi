from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvailabilityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknow1: _ClassVar[AvailabilityState]
    NotRunning: _ClassVar[AvailabilityState]
    RuningRecent: _ClassVar[AvailabilityState]
    Unknow2: _ClassVar[AvailabilityState]
    Unknow3: _ClassVar[AvailabilityState]
    RunningWithKeyInCar: _ClassVar[AvailabilityState]

class AvailabilityBool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknow4: _ClassVar[AvailabilityBool]
    No: _ClassVar[AvailabilityBool]
    Yes: _ClassVar[AvailabilityBool]
Unknow1: AvailabilityState
NotRunning: AvailabilityState
RuningRecent: AvailabilityState
Unknow2: AvailabilityState
Unknow3: AvailabilityState
RunningWithKeyInCar: AvailabilityState
Unknow4: AvailabilityBool
No: AvailabilityBool
Yes: AvailabilityBool

class GetAvailabilityReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class AvailabilityDataHead(_message.Message):
    __slots__ = ("updateTime", "unknown1")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    updateTime: int
    unknown1: int
    def __init__(self, updateTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class AvailabilityData(_message.Message):
    __slots__ = ("head", "engineLocalRunning", "engineRunningState")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ENGINELOCALRUNNING_FIELD_NUMBER: _ClassVar[int]
    ENGINERUNNINGSTATE_FIELD_NUMBER: _ClassVar[int]
    head: AvailabilityDataHead
    engineLocalRunning: AvailabilityBool
    engineRunningState: AvailabilityState
    def __init__(self, head: _Optional[_Union[AvailabilityDataHead, _Mapping]] = ..., engineLocalRunning: _Optional[_Union[AvailabilityBool, str]] = ..., engineRunningState: _Optional[_Union[AvailabilityState, str]] = ...) -> None: ...

class GetAvailabilityResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: AvailabilityData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[AvailabilityData, _Mapping]] = ...) -> None: ...
