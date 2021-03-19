# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def prepare_httpsuccess_head200(**kwargs: Any) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="HEAD",
        url=url,
    )


def prepare_httpsuccess_head204(**kwargs: Any) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="HEAD",
        url=url,
    )


def prepare_httpsuccess_head404(**kwargs: Any) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/404")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="HEAD",
        url=url,
    )
