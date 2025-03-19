from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLastKnownLocationsReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class otherLocationUnknowData(_message.Message):
    __slots__ = ("unknow3", "unknow4")
    UNKNOW3_FIELD_NUMBER: _ClassVar[int]
    UNKNOW4_FIELD_NUMBER: _ClassVar[int]
    unknow3: int
    unknow4: int
    def __init__(self, unknow3: _Optional[int] = ..., unknow4: _Optional[int] = ...) -> None: ...

class otherLocations(_message.Message):
    __slots__ = ("longitude", "latitude", "unknow2")
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    UNKNOW2_FIELD_NUMBER: _ClassVar[int]
    longitude: float
    latitude: float
    unknow2: otherLocationUnknowData
    def __init__(self, longitude: _Optional[float] = ..., latitude: _Optional[float] = ..., unknow2: _Optional[_Union[otherLocationUnknowData, _Mapping]] = ...) -> None: ...

class StreamLastKnownLocationsResp(_message.Message):
    __slots__ = ("vin", "longitude", "latitude", "unknow1", "other")
    VIN_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    UNKNOW1_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_NUMBER: _ClassVar[int]
    vin: str
    longitude: float
    latitude: float
    unknow1: int
    other: otherLocations
    def __init__(self, vin: _Optional[str] = ..., longitude: _Optional[float] = ..., latitude: _Optional[float] = ..., unknow1: _Optional[int] = ..., other: _Optional[_Union[otherLocations, _Mapping]] = ...) -> None: ...
