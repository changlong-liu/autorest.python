# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, List, Optional

_SERIALIZER = Serializer()


def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)


# fmt: off

def build_get_boolean_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    bool_path = True
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/bool/true/{boolPath}')
    path_format_arguments = {
        "boolPath": _SERIALIZER.url("bool_path", bool_path, 'bool'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_boolean_false_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get false Boolean value on path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    bool_path = False
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/bool/false/{boolPath}')
    path_format_arguments = {
        "boolPath": _SERIALIZER.url("bool_path", bool_path, 'bool'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_int_one_million_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '1000000' integer value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    int_path = 1000000
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/int/1000000/{intPath}')
    path_format_arguments = {
        "intPath": _SERIALIZER.url("int_path", int_path, 'int'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_int_negative_one_million_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '-1000000' integer value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    int_path = -1000000
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/int/-1000000/{intPath}')
    path_format_arguments = {
        "intPath": _SERIALIZER.url("int_path", int_path, 'int'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_ten_billion_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '10000000000' 64 bit integer value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    long_path = 10000000000
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/long/10000000000/{longPath}')
    path_format_arguments = {
        "longPath": _SERIALIZER.url("long_path", long_path, 'long'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_negative_ten_billion_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '-10000000000' 64 bit integer value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    long_path = -10000000000
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/long/-10000000000/{longPath}')
    path_format_arguments = {
        "longPath": _SERIALIZER.url("long_path", long_path, 'long'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_float_scientific_positive_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '1.034E+20' numeric value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    float_path = 103400000000000000000
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/float/1.034E+20/{floatPath}')
    path_format_arguments = {
        "floatPath": _SERIALIZER.url("float_path", float_path, 'float'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_float_scientific_negative_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '-1.034E-20' numeric value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    float_path = -1.034e-20
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/float/-1.034E-20/{floatPath}')
    path_format_arguments = {
        "floatPath": _SERIALIZER.url("float_path", float_path, 'float'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_double_decimal_positive_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '9999999.999' numeric value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    double_path = 9999999.999
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/double/9999999.999/{doublePath}')
    path_format_arguments = {
        "doublePath": _SERIALIZER.url("double_path", double_path, 'float'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_double_decimal_negative_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '-9999999.999' numeric value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    double_path = -9999999.999
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/double/-9999999.999/{doublePath}')
    path_format_arguments = {
        "doublePath": _SERIALIZER.url("double_path", double_path, 'float'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_string_unicode_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '啊齄丂狛狜隣郎隣兀﨩' multi-byte string value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    string_path = "啊齄丂狛狜隣郎隣兀﨩"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/unicode/{stringPath}')
    path_format_arguments = {
        "stringPath": _SERIALIZER.url("string_path", string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_string_url_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get 'begin!*'();:@ &=+$,/?#[]end.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    string_path = "begin!*'();:@ &=+$,/?#[]end"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/begin%21%2A%27%28%29%3B%3A%40%20%26%3D%2B%24%2C%2F%3F%23%5B%5Dend/{stringPath}')
    path_format_arguments = {
        "stringPath": _SERIALIZER.url("string_path", string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_string_url_non_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get 'begin!*'();:@&=+$,end.

    https://tools.ietf.org/html/rfc3986#appendix-A 'path' accept any 'pchar' not encoded.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    string_path = "begin!*'();:@&=+$,end"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/begin!*\'();:@&=+$,end/{stringPath}')
    path_format_arguments = {
        "stringPath": _SERIALIZER.url("string_path", string_path, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_string_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get ''.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    string_path = ""
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/empty/{stringPath}')
    path_format_arguments = {
        "stringPath": _SERIALIZER.url("string_path", string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_string_null_request(
    string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null (should throw).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param string_path: null string value.
    :type string_path: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/null/{stringPath}')
    path_format_arguments = {
        "stringPath": _SERIALIZER.url("string_path", string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_enum_valid_request(
    enum_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get using uri with 'green color' in path parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param enum_path: send the value green. Possible values are: "red color", "green color", and
     "blue color".
    :type enum_path: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/enum/green%20color/{enumPath}')
    path_format_arguments = {
        "enumPath": _SERIALIZER.url("enum_path", enum_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_enum_null_request(
    enum_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null (should throw on the client before the request is sent on wire).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param enum_path: send null should throw. Possible values are: "red color", "green color", and
     "blue color".
    :type enum_path: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/null/{enumPath}')
    path_format_arguments = {
        "enumPath": _SERIALIZER.url("enum_path", enum_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_byte_multi_byte_request(
    byte_path,  # type: bytearray
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '啊齄丂狛狜隣郎隣兀﨩' multibyte value as utf-8 encoded byte array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param byte_path: '啊齄丂狛狜隣郎隣兀﨩' multibyte value as utf-8 encoded byte array.
    :type byte_path: bytearray
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/byte/multibyte/{bytePath}')
    path_format_arguments = {
        "bytePath": _SERIALIZER.url("byte_path", byte_path, 'bytearray'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_byte_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '' as byte array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    byte_path = bytearray("", encoding="utf-8")
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/byte/empty/{bytePath}')
    path_format_arguments = {
        "bytePath": _SERIALIZER.url("byte_path", byte_path, 'bytearray'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_byte_null_request(
    byte_path,  # type: bytearray
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null as byte array (should throw).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param byte_path: null as byte array (should throw).
    :type byte_path: bytearray
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/byte/null/{bytePath}')
    path_format_arguments = {
        "bytePath": _SERIALIZER.url("byte_path", byte_path, 'bytearray'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_date_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '2012-01-01' as date.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    date_path = "2012-01-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/date/2012-01-01/{datePath}')
    path_format_arguments = {
        "datePath": _SERIALIZER.url("date_path", date_path, 'date'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_date_null_request(
    date_path,  # type: datetime.date
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null as date - this should throw or be unusable on the client side, depending on date
    representation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param date_path: null as date (should throw).
    :type date_path: ~datetime.date
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/date/null/{datePath}')
    path_format_arguments = {
        "datePath": _SERIALIZER.url("date_path", date_path, 'date'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_date_time_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get '2012-01-01T01:01:01Z' as date-time.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    date_time_path = "2012-01-01T01:01:01Z"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/datetime/2012-01-01T01%3A01%3A01Z/{dateTimePath}')
    path_format_arguments = {
        "dateTimePath": _SERIALIZER.url("date_time_path", date_time_path, 'iso-8601'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_date_time_null_request(
    date_time_path,  # type: datetime.datetime
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null as date-time, should be disallowed or throw depending on representation of date-time.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param date_time_path: null as date-time.
    :type date_time_path: ~datetime.datetime
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/datetime/null/{dateTimePath}')
    path_format_arguments = {
        "dateTimePath": _SERIALIZER.url("date_time_path", date_time_path, 'iso-8601'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_base64_url_request(
    base64_url_path,  # type: bytes
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get 'lorem' encoded value as 'bG9yZW0' (base64url).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param base64_url_path: base64url encoded value.
    :type base64_url_path: bytes
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/string/bG9yZW0/{base64UrlPath}')
    path_format_arguments = {
        "base64UrlPath": _SERIALIZER.url("base64_url_path", base64_url_path, 'base64'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_array_csv_in_path_request(
    array_path,  # type: List[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get an array of string ['ArrayPath1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
    csv-array format.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param array_path: an array of string ['ArrayPath1', 'begin!*'();:@ &=+$,/?#[]end' , null, '']
     using the csv-array format.
    :type array_path: list[str]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/array/ArrayPath1%2cbegin%21%2A%27%28%29%3B%3A%40%20%26%3D%2B%24%2C%2F%3F%23%5B%5Dend%2c%2c/{arrayPath}')
    path_format_arguments = {
        "arrayPath": _SERIALIZER.url("array_path", array_path, '[str]', div=','),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_unix_time_url_request(
    unix_time_url_path,  # type: datetime.datetime
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get the date 2016-04-13 encoded value as '1460505600' (Unix time).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param unix_time_url_path: Unix time encoded value.
    :type unix_time_url_path: ~datetime.datetime
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paths/int/1460505600/{unixTimeUrlPath}')
    path_format_arguments = {
        "unixTimeUrlPath": _SERIALIZER.url("unix_time_url_path", unix_time_url_path, 'unix-time'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )
