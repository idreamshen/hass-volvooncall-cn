from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor


class LockStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_STATUS_UNSPECIFIED: _ClassVar[LockStatus]
    LOCK_STATUS_UNLOCKED: _ClassVar[LockStatus]
    LOCK_STATUS_LOCKED: _ClassVar[LockStatus]


class OpenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPEN_STATUS_UNSPECIFIED: _ClassVar[OpenStatus]
    OPEN_STATUS_OPEN: _ClassVar[OpenStatus]
    OPEN_STATUS_CLOSED: _ClassVar[OpenStatus]
    OPEN_STATUS_AJAR: _ClassVar[OpenStatus]


LOCK_STATUS_UNSPECIFIED: LockStatus
LOCK_STATUS_UNLOCKED: LockStatus
LOCK_STATUS_LOCKED: LockStatus
OPEN_STATUS_UNSPECIFIED: OpenStatus
OPEN_STATUS_OPEN: OpenStatus
OPEN_STATUS_CLOSED: OpenStatus
OPEN_STATUS_AJAR: OpenStatus


class GetExteriorReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...


class TimeStamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...


class ExteriorStatus(_message.Message):
    __slots__ = ("timestamp", "central_lock", "front_left_door", "front_right_door", "rear_left_door", "rear_right_door", "front_left_window",
                 "front_right_window", "rear_left_window", "rear_right_window", "hood", "tailgate", "tank_lid", "sunroof", "unknow1")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CENTRAL_LOCK_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_DOOR_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_DOOR_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_DOOR_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_DOOR_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    HOOD_FIELD_NUMBER: _ClassVar[int]
    TAILGATE_FIELD_NUMBER: _ClassVar[int]
    TANK_LID_FIELD_NUMBER: _ClassVar[int]
    SUNROOF_FIELD_NUMBER: _ClassVar[int]
    UNKNOW1_FIELD_NUMBER: _ClassVar[int]
    timestamp: TimeStamp
    central_lock: LockStatus
    front_left_door: OpenStatus
    front_right_door: OpenStatus
    rear_left_door: OpenStatus
    rear_right_door: OpenStatus
    front_left_window: OpenStatus
    front_right_window: OpenStatus
    rear_left_window: OpenStatus
    rear_right_window: OpenStatus
    hood: OpenStatus
    tailgate: OpenStatus
    tank_lid: OpenStatus
    sunroof: OpenStatus
    unknow1: int
    def __init__(self, timestamp: _Optional[_Union[TimeStamp, _Mapping]] = ..., central_lock: _Optional[_Union[LockStatus, str]] = ..., front_left_door: _Optional[_Union[OpenStatus, str]] = ..., front_right_door: _Optional[_Union[OpenStatus, str]] = ..., rear_left_door: _Optional[_Union[OpenStatus, str]] = ..., rear_right_door: _Optional[_Union[OpenStatus, str]] = ..., front_left_window: _Optional[_Union[OpenStatus, str]] = ...,
                 front_right_window: _Optional[_Union[OpenStatus, str]] = ..., rear_left_window: _Optional[_Union[OpenStatus, str]] = ..., rear_right_window: _Optional[_Union[OpenStatus, str]] = ..., hood: _Optional[_Union[OpenStatus, str]] = ..., tailgate: _Optional[_Union[OpenStatus, str]] = ..., tank_lid: _Optional[_Union[OpenStatus, str]] = ..., sunroof: _Optional[_Union[OpenStatus, str]] = ..., unknow1: _Optional[int] = ...) -> None: ...


class GetExteriorResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: ExteriorStatus
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[ExteriorStatus, _Mapping]] = ...) -> None: ...
