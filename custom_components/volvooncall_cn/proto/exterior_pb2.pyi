from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetExteriorReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class ExteriorDataHeader(_message.Message):
    __slots__ = ("updateTime", "unknown1")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    updateTime: int
    unknown1: int
    def __init__(self, updateTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class ExteriorData(_message.Message):
    __slots__ = ("header", "lock", "frontLeftDoor", "frontRightDoor", "rearLeftDoor", "rearRightDoor", "frontLeftWindow", "frontRightWindow", "rearLeftWindow", "rearRightWindow", "hood", "tailGate", "unknown3", "sunRoof", "unknown4")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    FRONTLEFTDOOR_FIELD_NUMBER: _ClassVar[int]
    FRONTRIGHTDOOR_FIELD_NUMBER: _ClassVar[int]
    REARLEFTDOOR_FIELD_NUMBER: _ClassVar[int]
    REARRIGHTDOOR_FIELD_NUMBER: _ClassVar[int]
    FRONTLEFTWINDOW_FIELD_NUMBER: _ClassVar[int]
    FRONTRIGHTWINDOW_FIELD_NUMBER: _ClassVar[int]
    REARLEFTWINDOW_FIELD_NUMBER: _ClassVar[int]
    REARRIGHTWINDOW_FIELD_NUMBER: _ClassVar[int]
    HOOD_FIELD_NUMBER: _ClassVar[int]
    TAILGATE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
    SUNROOF_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
    header: ExteriorDataHeader
    lock: int
    frontLeftDoor: int
    frontRightDoor: int
    rearLeftDoor: int
    rearRightDoor: int
    frontLeftWindow: int
    frontRightWindow: int
    rearLeftWindow: int
    rearRightWindow: int
    hood: int
    tailGate: int
    unknown3: int
    sunRoof: int
    unknown4: int
    def __init__(self, header: _Optional[_Union[ExteriorDataHeader, _Mapping]] = ..., lock: _Optional[int] = ..., frontLeftDoor: _Optional[int] = ..., frontRightDoor: _Optional[int] = ..., rearLeftDoor: _Optional[int] = ..., rearRightDoor: _Optional[int] = ..., frontLeftWindow: _Optional[int] = ..., frontRightWindow: _Optional[int] = ..., rearLeftWindow: _Optional[int] = ..., rearRightWindow: _Optional[int] = ..., hood: _Optional[int] = ..., tailGate: _Optional[int] = ..., unknown3: _Optional[int] = ..., sunRoof: _Optional[int] = ..., unknown4: _Optional[int] = ...) -> None: ...

class GetExteriorResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: ExteriorData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[ExteriorData, _Mapping]] = ...) -> None: ...
