from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvailabilityReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unspecified1: _ClassVar[AvailabilityReason]
    NoInternet: _ClassVar[AvailabilityReason]
    PowerSavingMode: _ClassVar[AvailabilityReason]
    CarInUse: _ClassVar[AvailabilityReason]
    OtaInstallationInProgress: _ClassVar[AvailabilityReason]
    Unknow1: _ClassVar[AvailabilityReason]
    Unknow2: _ClassVar[AvailabilityReason]
    Unknow3: _ClassVar[AvailabilityReason]

class AvailabilityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unspecified2: _ClassVar[AvailabilityStatus]
    Available: _ClassVar[AvailabilityStatus]
    Unavailable: _ClassVar[AvailabilityStatus]
Unspecified1: AvailabilityReason
NoInternet: AvailabilityReason
PowerSavingMode: AvailabilityReason
CarInUse: AvailabilityReason
OtaInstallationInProgress: AvailabilityReason
Unknow1: AvailabilityReason
Unknow2: AvailabilityReason
Unknow3: AvailabilityReason
Unspecified2: AvailabilityStatus
Available: AvailabilityStatus
Unavailable: AvailabilityStatus

class GetAvailabilityReq(_message.Message):
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

class AvailabilityData(_message.Message):
    __slots__ = ("updatetime", "availableStatus", "unavailableReason")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLESTATUS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLEREASON_FIELD_NUMBER: _ClassVar[int]
    updatetime: Timestamp
    availableStatus: AvailabilityStatus
    unavailableReason: AvailabilityReason
    def __init__(self, updatetime: _Optional[_Union[Timestamp, _Mapping]] = ..., availableStatus: _Optional[_Union[AvailabilityStatus, str]] = ..., unavailableReason: _Optional[_Union[AvailabilityReason, str]] = ...) -> None: ...

class GetAvailabilityResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: AvailabilityData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[AvailabilityData, _Mapping]] = ...) -> None: ...
