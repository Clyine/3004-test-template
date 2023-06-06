from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class inputObj(_message.Message):
    __slots__ = ["params1", "params2"]
    PARAMS1_FIELD_NUMBER: _ClassVar[int]
    PARAMS2_FIELD_NUMBER: _ClassVar[int]
    params1: int
    params2: int
    def __init__(self, params1: _Optional[int] = ..., params2: _Optional[int] = ...) -> None: ...

class resultObj(_message.Message):
    __slots__ = ["value1", "value2"]
    VALUE1_FIELD_NUMBER: _ClassVar[int]
    VALUE2_FIELD_NUMBER: _ClassVar[int]
    value1: int
    value2: int
    def __init__(self, value1: _Optional[int] = ..., value2: _Optional[int] = ...) -> None: ...
