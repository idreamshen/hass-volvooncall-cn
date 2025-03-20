from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFuelReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class FuelDataTimeInfo(_message.Message):
    __slots__ = ("lastRunTime", "unknown1")
    LASTRUNTIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    lastRunTime: int
    unknown1: int
    def __init__(self, lastRunTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class FuelData(_message.Message):
    __slots__ = ("timeInfo", "distanceToEmpty", "TMFuelAvgConsum", "fuelAmount", "unknown2", "ATFuleAvgConsum")
    TIMEINFO_FIELD_NUMBER: _ClassVar[int]
    DISTANCETOEMPTY_FIELD_NUMBER: _ClassVar[int]
    TMFUELAVGCONSUM_FIELD_NUMBER: _ClassVar[int]
    FUELAMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    ATFULEAVGCONSUM_FIELD_NUMBER: _ClassVar[int]
    timeInfo: FuelDataTimeInfo
    distanceToEmpty: int
    TMFuelAvgConsum: float
    fuelAmount: float
    unknown2: int
    ATFuleAvgConsum: float
    def __init__(self, timeInfo: _Optional[_Union[FuelDataTimeInfo, _Mapping]] = ..., distanceToEmpty: _Optional[int] = ..., TMFuelAvgConsum: _Optional[float] = ..., fuelAmount: _Optional[float] = ..., unknown2: _Optional[int] = ..., ATFuleAvgConsum: _Optional[float] = ...) -> None: ...

class GetFuelResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: FuelData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[FuelData, _Mapping]] = ...) -> None: ...
