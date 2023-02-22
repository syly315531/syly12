from typing import (
    Callable,
    Optional,
    Union,
    Any,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Tuple,
    IO,
    Text,
    Type,
    Dict,
)

from . import http_auth as auth
from .http_models import Response, PreparedRequest
from .http_cookies import RequestsCookieJar
from .http_sessions import HTTPSession

_ParamsMappingValueType = Union[
    str, bytes, int, float, Iterable[Union[str, bytes, int, float]]
]
Params = Optional[
    Union[
        Mapping[Union[str, bytes, int, float], _ParamsMappingValueType],
        Union[str, bytes],
        Tuple[Union[str, bytes, int, float], _ParamsMappingValueType],
        Mapping[str, _ParamsMappingValueType],
        Mapping[bytes, _ParamsMappingValueType],
        Mapping[int, _ParamsMappingValueType],
        Mapping[float, _ParamsMappingValueType],
    ]
]
Data = Union[
    None,
    bytes,
    MutableMapping[str, str],
    MutableMapping[str, Text],
    MutableMapping[Text, str],
    MutableMapping[Text, Text],
    Iterable[Tuple[str, str]],
    IO,
]
_Hook = Callable[[Response], Any]
Method = str
URL = str
Headers = Optional[Union[None, MutableMapping[Text, Text]]]
Cookies = Optional[Union[None, RequestsCookieJar, MutableMapping[Text, Text]]]
Files = Optional[MutableMapping[Text, IO]]
Auth = Union[
    None, Tuple[Text, Text], auth.AuthBase, Callable[[PreparedRequest], PreparedRequest]
]
Timeout = Union[None, float, Tuple[float, float]]
AllowRedirects = Optional[bool]
Proxies = Optional[MutableMapping[Text, Text]]
Hooks = Optional[MutableMapping[Text, Union[Iterable[_Hook], _Hook]]]
Stream = Optional[bool]
Verify = Union[None, bool, Text]
Cert = Union[Text, Tuple[Text, Text]]
JSON = Optional[MutableMapping]
Help = Dict
Host = str
Sequence = List
Filename = str
KeyValueList = List[Tuple[Text, Text]]
