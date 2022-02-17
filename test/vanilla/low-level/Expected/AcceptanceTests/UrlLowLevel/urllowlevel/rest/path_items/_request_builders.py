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

def build_get_all_with_values_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    path_item_string_query = kwargs.pop('path_item_string_query', _get_from_dict(_params, 'pathItemStringQuery') or None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', _get_from_dict(_params, 'globalStringQuery') or None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', _get_from_dict(_params, 'localStringQuery') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        _params['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        _params['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_global_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    path_item_string_query = kwargs.pop('path_item_string_query', _get_from_dict(_params, 'pathItemStringQuery') or None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', _get_from_dict(_params, 'globalStringQuery') or None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', _get_from_dict(_params, 'localStringQuery') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        _params['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        _params['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_global_and_local_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain null value. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    path_item_string_query = kwargs.pop('path_item_string_query', _get_from_dict(_params, 'pathItemStringQuery') or None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', _get_from_dict(_params, 'globalStringQuery') or None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', _get_from_dict(_params, 'localStringQuery') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        _params['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        _params['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_local_path_item_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery=null, localStringQuery=null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: should contain value null. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value null. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    path_item_string_query = kwargs.pop('path_item_string_query', _get_from_dict(_params, 'pathItemStringQuery') or None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', _get_from_dict(_params, 'globalStringQuery') or None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', _get_from_dict(_params, 'localStringQuery') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        _params['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        _params['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
