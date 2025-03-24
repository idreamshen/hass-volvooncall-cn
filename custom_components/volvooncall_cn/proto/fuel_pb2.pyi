from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFuelReq(_message.Message):
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

class FuelData(_message.Message):
    __slots__ = ("updateTime", "distanceToEmptyKm", "TMFuelAvgConsum", "fuelAmount", "distanceToEmptyMiles", "ATFuleAvgConsum")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    DISTANCETOEMPTYKM_FIELD_NUMBER: _ClassVar[int]
    TMFUELAVGCONSUM_FIELD_NUMBER: _ClassVar[int]
    FUELAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISTANCETOEMPTYMILES_FIELD_NUMBER: _ClassVar[int]
    ATFULEAVGCONSUM_FIELD_NUMBER: _ClassVar[int]
    updateTime: Timestamp
    distanceToEmptyKm: int
    TMFuelAvgConsum: float
    fuelAmount: float
    distanceToEmptyMiles: int
    ATFuleAvgConsum: float
    def __init__(self, updateTime: _Optional[_Union[Timestamp, _Mapping]] = ..., distanceToEmptyKm: _Optional[int] = ..., TMFuelAvgConsum: _Optional[float] = ..., fuelAmount: _Optional[float] = ..., distanceToEmptyMiles: _Optional[int] = ..., ATFuleAvgConsum: _Optional[float] = ...) -> None: ...

class GetFuelResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: FuelData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[FuelData, _Mapping]] = ...) -> None: ...
