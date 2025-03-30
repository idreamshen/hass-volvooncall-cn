from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPreferencesReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class Preference(_message.Message):
    __slots__ = ("nickName",)
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    nickName: str
    def __init__(self, nickName: _Optional[str] = ...) -> None: ...

class GetPreferencesResp(_message.Message):
    __slots__ = ("preference",)
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    preference: Preference
    def __init__(self, preference: _Optional[_Union[Preference, _Mapping]] = ...) -> None: ...

class UpdatePreferencesReq(_message.Message):
    __slots__ = ("vin", "preference")
    VIN_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    vin: str
    preference: Preference
    def __init__(self, vin: _Optional[str] = ..., preference: _Optional[_Union[Preference, _Mapping]] = ...) -> None: ...

class UpdatePreferencesResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
