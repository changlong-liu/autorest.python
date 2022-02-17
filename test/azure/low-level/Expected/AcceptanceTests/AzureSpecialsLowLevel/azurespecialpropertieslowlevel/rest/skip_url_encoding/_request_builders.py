# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.rest import HttpRequest

from ..._vendor import _format_url_section, _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_method_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
    :type unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}"
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
    :type unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}"
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_swagger_path_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword unencoded_path_param: An unencoded path parameter with value 'path1/path2/path3'.
     Default value is "path1/path2/path3". Note that overriding this default value may result in
     unsupported behavior.
    :paramtype unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    unencoded_path_param = kwargs.pop('unencoded_path_param', "path1/path2/path3")  # type: str
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}"
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_method_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    q1 = kwargs.pop('q1')  # type: str
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/method/query/valid"

    # Construct parameters
    _params['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_method_query_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded query parameter with value null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value null. Default value is None.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    q1 = kwargs.pop('q1', _get_from_dict(_params, 'q1') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/method/query/null"

    # Construct parameters
    if q1 is not None:
        _params['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_path_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    q1 = kwargs.pop('q1')  # type: str
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/path/query/valid"

    # Construct parameters
    _params['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_swagger_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: An unencoded query parameter with value 'value1&q2=value2&q3=value3'. Default
     value is "value1&q2=value2&q3=value3". Note that overriding this default value may result in
     unsupported behavior.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    q1 = kwargs.pop('q1', _get_from_dict(_params, 'q1') or "value1&q2=value2&q3=value3")  # type: str
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/azurespecials/skipUrlEncoding/swagger/query/valid"

    # Construct parameters
    _params['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
