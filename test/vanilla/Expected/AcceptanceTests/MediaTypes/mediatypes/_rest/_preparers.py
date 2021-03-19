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
    from typing import Any, IO, Optional, Union

_SERIALIZER = Serializer()


def prepare_analyze_body(
    input=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/analyze")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    if header_parameters["Content-Type"].split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["content"] = input

    elif header_parameters["Content-Type"].split(";")[0] in ["application/json"]:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["json"] = input
    else:
        raise ValueError(
            "The content_type '{}' is not one of the allowed values: "
            "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(
                header_parameters["Content-Type"]
            )
        )

    return HttpRequest(method="POST", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_content_type_with_encoding(
    input=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "text/plain")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/contentTypeWithEncoding")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = input

    return HttpRequest(method="POST", url=url, headers=header_parameters, **body_content_kwargs)
