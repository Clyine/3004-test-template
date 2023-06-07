from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class bid(_message.Message):
    __slots__ = ["bidder", "itemName", "price"]
    BIDDER_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    bidder: str
    itemName: str
    price: int
    def __init__(self, itemName: _Optional[str] = ..., bidder: _Optional[str] = ..., price: _Optional[int] = ...) -> None: ...

class item(_message.Message):
    __slots__ = ["itemName"]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    itemName: str
    def __init__(self, itemName: _Optional[str] = ...) -> None: ...

class result(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class systemList(_message.Message):
    __slots__ = ["bidlist"]
    BIDLIST_FIELD_NUMBER: _ClassVar[int]
    bidlist: _containers.RepeatedCompositeFieldContainer[bid]
    def __init__(self, bidlist: _Optional[_Iterable[_Union[bid, _Mapping]]] = ...) -> None: ...
