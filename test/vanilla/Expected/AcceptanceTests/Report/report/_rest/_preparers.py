# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()


def prepare_get_report(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    qualifier = kwargs.pop("qualifier", None)  # type: Optional[str]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/report")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters["qualifier"] = _SERIALIZER.query("qualifier", qualifier, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_get_optional_report(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    qualifier = kwargs.pop("qualifier", None)  # type: Optional[str]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/report/optional")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters["qualifier"] = _SERIALIZER.query("qualifier", qualifier, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
