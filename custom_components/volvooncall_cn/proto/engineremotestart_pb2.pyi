from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EngineErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unspecifid1: _ClassVar[EngineErrorType]
    ExceededMaxAttempt: _ClassVar[EngineErrorType]
    CarUnLocked: _ClassVar[EngineErrorType]
    KeyInCar: _ClassVar[EngineErrorType]
    DoorOpen: _ClassVar[EngineErrorType]
    HoodOpen: _ClassVar[EngineErrorType]
    IncorrectGear: _ClassVar[EngineErrorType]
    PersonInCar: _ClassVar[EngineErrorType]
    PedalPressed: _ClassVar[EngineErrorType]
    LowFuel: _ClassVar[EngineErrorType]
    LowBattery: _ClassVar[EngineErrorType]
    LowBatteryAndFuel: _ClassVar[EngineErrorType]
    ChargerPlugged: _ClassVar[EngineErrorType]
    EngineCoolantFault: _ClassVar[EngineErrorType]
    BatteryCoolantFault: _ClassVar[EngineErrorType]
    ServiceRequired: _ClassVar[EngineErrorType]
    Other: _ClassVar[EngineErrorType]

class EngineRunningStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unspecifid2: _ClassVar[EngineRunningStatus]
    Off: _ClassVar[EngineRunningStatus]
    Starting: _ClassVar[EngineRunningStatus]
    Running: _ClassVar[EngineRunningStatus]
    Stopping: _ClassVar[EngineRunningStatus]
Unspecifid1: EngineErrorType
ExceededMaxAttempt: EngineErrorType
CarUnLocked: EngineErrorType
KeyInCar: EngineErrorType
DoorOpen: EngineErrorType
HoodOpen: EngineErrorType
IncorrectGear: EngineErrorType
PersonInCar: EngineErrorType
PedalPressed: EngineErrorType
LowFuel: EngineErrorType
LowBattery: EngineErrorType
LowBatteryAndFuel: EngineErrorType
ChargerPlugged: EngineErrorType
EngineCoolantFault: EngineErrorType
BatteryCoolantFault: EngineErrorType
ServiceRequired: EngineErrorType
Other: EngineErrorType
Unspecifid2: EngineRunningStatus
Off: EngineRunningStatus
Starting: EngineRunningStatus
Running: EngineRunningStatus
Stopping: EngineRunningStatus

class GetEngineRemoteStartReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class GetEngineRemoteStartData(_message.Message):
    __slots__ = ("updateTime", "engineRunningStatus", "engineError", "engineStartTime", "engineEndTime")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    ENGINERUNNINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    ENGINEERROR_FIELD_NUMBER: _ClassVar[int]
    ENGINESTARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENGINEENDTIME_FIELD_NUMBER: _ClassVar[int]
    updateTime: Timestamp
    engineRunningStatus: EngineRunningStatus
    engineError: EngineErrorType
    engineStartTime: int
    engineEndTime: int
    def __init__(self, updateTime: _Optional[_Union[Timestamp, _Mapping]] = ..., engineRunningStatus: _Optional[_Union[EngineRunningStatus, str]] = ..., engineError: _Optional[_Union[EngineErrorType, str]] = ..., engineStartTime: _Optional[int] = ..., engineEndTime: _Optional[int] = ...) -> None: ...

class GetEngineRemoteStartResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: GetEngineRemoteStartData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[GetEngineRemoteStartData, _Mapping]] = ...) -> None: ...
