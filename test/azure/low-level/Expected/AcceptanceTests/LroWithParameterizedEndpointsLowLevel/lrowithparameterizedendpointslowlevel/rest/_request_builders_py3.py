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

from .._vendor import _format_url_section, _get_from_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_poll_with_parameterized_endpoints_request(**kwargs: Any) -> HttpRequest:
    """Poll with method and client level parameters in endpoint.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    _url = "/lroParameterizedEndpoints"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_poll_with_constant_parameterized_endpoints_request(**kwargs: Any) -> HttpRequest:
    """Poll with method and client level parameters in endpoint, with a constant value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_parameter: Next link for the list operation. Default value is "iAmConstant".
     Note that overriding this default value may result in unsupported behavior.
    :paramtype constant_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    constant_parameter = kwargs.pop("constant_parameter", "iAmConstant")  # type: str
    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    _url = "/lroConstantParameterizedEndpoints/{constantParameter}"
    path_format_arguments = {
        "constantParameter": _SERIALIZER.url("constant_parameter", constant_parameter, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)
