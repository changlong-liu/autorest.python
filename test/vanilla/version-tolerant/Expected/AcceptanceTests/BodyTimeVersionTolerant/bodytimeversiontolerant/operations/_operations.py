# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Optional, TypeVar, cast

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_time_get_request(**kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/time/get"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_time_put_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/time/put"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


class TimeOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodytimeversiontolerant.AutoRestTimeTestService`'s
        :attr:`time` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(self, **kwargs: Any) -> datetime.time:
        """Get time value "11:34:56".

        :return: time
        :rtype: ~datetime.time
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.time]

        request = build_time_get_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(datetime.time, deserialized), {})

        return cast(datetime.time, deserialized)

    @distributed_trace
    def put(self, time_body: datetime.time, **kwargs: Any) -> str:
        """Put time value "08:07:56".

        :param time_body: Put time value "08:07:56" in parameter to pass testserver.
        :type time_body: ~datetime.time
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = time_body

        request = build_time_put_request(
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)
