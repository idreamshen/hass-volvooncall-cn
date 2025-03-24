from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOdometerReq(_message.Message):
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

class odometerData(_message.Message):
    __slots__ = ("updateTime", "odometerMeters", "tripMeterManualKm", "tripMeterAutomaticKm", "averageSpeedKmPerHour", "averageSpeedKmPerHourAutomatic", "tripMeterSinceChargeKm", "averageSpeedKmPerHourSinceCharge")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    ODOMETERMETERS_FIELD_NUMBER: _ClassVar[int]
    TRIPMETERMANUALKM_FIELD_NUMBER: _ClassVar[int]
    TRIPMETERAUTOMATICKM_FIELD_NUMBER: _ClassVar[int]
    AVERAGESPEEDKMPERHOUR_FIELD_NUMBER: _ClassVar[int]
    AVERAGESPEEDKMPERHOURAUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    TRIPMETERSINCECHARGEKM_FIELD_NUMBER: _ClassVar[int]
    AVERAGESPEEDKMPERHOURSINCECHARGE_FIELD_NUMBER: _ClassVar[int]
    updateTime: Timestamp
    odometerMeters: int
    tripMeterManualKm: float
    tripMeterAutomaticKm: float
    averageSpeedKmPerHour: int
    averageSpeedKmPerHourAutomatic: int
    tripMeterSinceChargeKm: int
    averageSpeedKmPerHourSinceCharge: int
    def __init__(self, updateTime: _Optional[_Union[Timestamp, _Mapping]] = ..., odometerMeters: _Optional[int] = ..., tripMeterManualKm: _Optional[float] = ..., tripMeterAutomaticKm: _Optional[float] = ..., averageSpeedKmPerHour: _Optional[int] = ..., averageSpeedKmPerHourAutomatic: _Optional[int] = ..., tripMeterSinceChargeKm: _Optional[int] = ..., averageSpeedKmPerHourSinceCharge: _Optional[int] = ...) -> None: ...

class GetOdometerResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: odometerData
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[odometerData, _Mapping]] = ...) -> None: ...
