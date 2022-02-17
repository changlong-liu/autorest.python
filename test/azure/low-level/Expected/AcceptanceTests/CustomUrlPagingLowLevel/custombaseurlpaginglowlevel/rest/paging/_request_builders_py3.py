# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict

from msrest import Serializer

from azure.core.rest import HttpRequest

from ..._vendor import _format_url_section, _get_from_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_pages_partial_url_request(**kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL and expect to concat after
    host.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    _url = "/paging/customurl/partialnextlink"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_get_pages_partial_url_operation_request(**kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL with next operation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    _url = "/paging/customurl/partialnextlinkop"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_get_pages_partial_url_operation_next_request(next_link: str, **kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param next_link: Next link for the list operation.
    :type next_link: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    _url = "/paging/customurl/{nextLink}"
    path_format_arguments = {
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)
