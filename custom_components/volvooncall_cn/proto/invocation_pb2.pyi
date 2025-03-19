from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EngineStartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Stop: _ClassVar[EngineStartType]
    Start: _ClassVar[EngineStartType]
Stop: EngineStartType
Start: EngineStartType

class invocationHead(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class windowControlReq(_message.Message):
    __slots__ = ("head", "openType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    OPENTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    openType: int
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., openType: _Optional[int] = ...) -> None: ...

class windowData(_message.Message):
    __slots__ = ("deviceid", "vin", "timestamp")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deviceid: str
    vin: str
    timestamp: int
    def __init__(self, deviceid: _Optional[str] = ..., vin: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class invocationData(_message.Message):
    __slots__ = ("deviceid", "vin", "openType", "timestamp")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    OPENTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deviceid: str
    vin: str
    openType: int
    timestamp: int
    def __init__(self, deviceid: _Optional[str] = ..., vin: _Optional[str] = ..., openType: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class windowControlResp(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[invocationData]
    def __init__(self, data: _Optional[_Iterable[_Union[invocationData, _Mapping]]] = ...) -> None: ...

class EngineStartReq(_message.Message):
    __slots__ = ("head", "openType", "startDurationMin")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    OPENTYPE_FIELD_NUMBER: _ClassVar[int]
    STARTDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    openType: EngineStartType
    startDurationMin: int
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., openType: _Optional[_Union[EngineStartType, str]] = ..., startDurationMin: _Optional[int] = ...) -> None: ...

class EngineStartResp(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[invocationData]
    def __init__(self, data: _Optional[_Iterable[_Union[invocationData, _Mapping]]] = ...) -> None: ...

class HonkFlashReq(_message.Message):
    __slots__ = ("head", "onlyFlash")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ONLYFLASH_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    onlyFlash: int
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., onlyFlash: _Optional[int] = ...) -> None: ...

class HonkFlashResp(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[invocationData]
    def __init__(self, data: _Optional[_Iterable[_Union[invocationData, _Mapping]]] = ...) -> None: ...

class LockReq(_message.Message):
    __slots__ = ("head", "lockType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    LOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    lockType: int
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., lockType: _Optional[int] = ...) -> None: ...

class LockResp(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[invocationData]
    def __init__(self, data: _Optional[_Iterable[_Union[invocationData, _Mapping]]] = ...) -> None: ...
