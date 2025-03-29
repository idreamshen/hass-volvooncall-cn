from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class invocationControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[invocationControlType]
    OPEN: _ClassVar[invocationControlType]
    CLOSE: _ClassVar[invocationControlType]

class invocationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_ERROR: _ClassVar[invocationStatus]
    SENT: _ClassVar[invocationStatus]
    CAR_OFFLINE: _ClassVar[invocationStatus]
    DELIVERED: _ClassVar[invocationStatus]
    DELIVERY_TIMEOUT: _ClassVar[invocationStatus]
    SUCCESS: _ClassVar[invocationStatus]
    RESPONSE_TIMEOUT: _ClassVar[invocationStatus]
    UNKNOWN_CAR_ERROR: _ClassVar[invocationStatus]
    NOT_ALLOWED_PRIVACY_ENABLED: _ClassVar[invocationStatus]
    NOT_ALLOWED_WRONG_USAGE_MODE: _ClassVar[invocationStatus]
    INVOCATION_SPECIFIC_ERROR: _ClassVar[invocationStatus]
    NOT_ALLOWED_CONFLICTING_INVOCATION: _ClassVar[invocationStatus]

class HonkFlashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HONK_AND_FLASH: _ClassVar[HonkFlashType]
    HONK: _ClassVar[HonkFlashType]
    FLASH: _ClassVar[HonkFlashType]

class LockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK: _ClassVar[LockType]
    LOCK_REDUCED_GUARD: _ClassVar[LockType]

class UnlockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNLOCK_UNSPECIFIED: _ClassVar[UnlockType]
    TRUNK_ONLY: _ClassVar[UnlockType]
UNSPECIFIED: invocationControlType
OPEN: invocationControlType
CLOSE: invocationControlType
UNKNOWN_ERROR: invocationStatus
SENT: invocationStatus
CAR_OFFLINE: invocationStatus
DELIVERED: invocationStatus
DELIVERY_TIMEOUT: invocationStatus
SUCCESS: invocationStatus
RESPONSE_TIMEOUT: invocationStatus
UNKNOWN_CAR_ERROR: invocationStatus
NOT_ALLOWED_PRIVACY_ENABLED: invocationStatus
NOT_ALLOWED_WRONG_USAGE_MODE: invocationStatus
INVOCATION_SPECIFIC_ERROR: invocationStatus
NOT_ALLOWED_CONFLICTING_INVOCATION: invocationStatus
HONK_AND_FLASH: HonkFlashType
HONK: HonkFlashType
FLASH: HonkFlashType
LOCK: LockType
LOCK_REDUCED_GUARD: LockType
UNLOCK_UNSPECIFIED: UnlockType
TRUNK_ONLY: UnlockType

class invocationHead(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class invocationData(_message.Message):
    __slots__ = ("deviceid", "vin", "status", "msg", "timestamp")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deviceid: str
    vin: str
    status: invocationStatus
    msg: str
    timestamp: int
    def __init__(self, deviceid: _Optional[str] = ..., vin: _Optional[str] = ..., status: _Optional[_Union[invocationStatus, str]] = ..., msg: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class invocationCommResp(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: invocationData
    def __init__(self, data: _Optional[_Union[invocationData, _Mapping]] = ...) -> None: ...

class windowControlReq(_message.Message):
    __slots__ = ("head", "openType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    OPENTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    openType: invocationControlType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., openType: _Optional[_Union[invocationControlType, str]] = ...) -> None: ...

class EngineStartReq(_message.Message):
    __slots__ = ("head", "isStart", "startDurationMin")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ISSTART_FIELD_NUMBER: _ClassVar[int]
    STARTDURATIONMIN_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    isStart: bool
    startDurationMin: int
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., isStart: bool = ..., startDurationMin: _Optional[int] = ...) -> None: ...

class HonkFlashReq(_message.Message):
    __slots__ = ("head", "honkFlashType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    HONKFLASHTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    honkFlashType: HonkFlashType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., honkFlashType: _Optional[_Union[HonkFlashType, str]] = ...) -> None: ...

class LockReq(_message.Message):
    __slots__ = ("head", "lockType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    LOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    lockType: LockType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., lockType: _Optional[_Union[LockType, str]] = ...) -> None: ...

class UnlockReq(_message.Message):
    __slots__ = ("head", "unlockType")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    UNLOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    unlockType: UnlockType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., unlockType: _Optional[_Union[UnlockType, str]] = ...) -> None: ...

class TailgateControlReq(_message.Message):
    __slots__ = ("head", "type")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    type: invocationControlType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., type: _Optional[_Union[invocationControlType, str]] = ...) -> None: ...

class SunroofControlReq(_message.Message):
    __slots__ = ("head", "type")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    type: invocationControlType
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ..., type: _Optional[_Union[invocationControlType, str]] = ...) -> None: ...

class UpdateStatusReq(_message.Message):
    __slots__ = ("head",)
    HEAD_FIELD_NUMBER: _ClassVar[int]
    head: invocationHead
    def __init__(self, head: _Optional[_Union[invocationHead, _Mapping]] = ...) -> None: ...
