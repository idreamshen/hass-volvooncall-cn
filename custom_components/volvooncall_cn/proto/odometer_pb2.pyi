from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOdometerReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class odometerDataHead(_message.Message):
    __slots__ = ("updateTime", "unknown1")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    updateTime: int
    unknown1: int
    def __init__(self, updateTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class odometerData(_message.Message):
    __slots__ = ("head", "totalDistance", "TMDistance", "TADistance", "TMAvgSpeed", "TAAvgSpeed")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TOTALDISTANCE_FIELD_NUMBER: _ClassVar[int]
    TMDISTANCE_FIELD_NUMBER: _ClassVar[int]
    TADISTANCE_FIELD_NUMBER: _ClassVar[int]
    TMAVGSPEED_FIELD_NUMBER: _ClassVar[int]
    TAAVGSPEED_FIELD_NUMBER: _ClassVar[int]
    head: odometerDataHead
    totalDistance: int
    TMDistance: float
    TADistance: float
    TMAvgSpeed: int
    TAAvgSpeed: int
    def __init__(self, head: _Optional[_Union[odometerDataHead, _Mapping]] = ..., totalDistance: _Optional[int] = ..., TMDistance: _Optional[float] = ..., TADistance: _Optional[float] = ..., TMAvgSpeed: _Optional[int] = ..., TAAvgSpeed: _Optional[int] = ...) -> None: ...

class GetOdometerResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: odometerData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[odometerData, _Mapping]] = ...) -> None: ...
