# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import json
from typing import TYPE_CHECKING
import warnings

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

from .. import models as _models
from .._rest import *

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class datetimerfc1123Operations(object):
    """datetimerfc1123Operations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydatetimerfc1123.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[datetime.datetime]
        """Get null datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or None, or the result of cls(response)
        :rtype: ~datetime.datetime or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[datetime.datetime]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_null_request(template_url=self.get_null.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/datetimerfc1123/null"}  # type: ignore

    @distributed_trace
    def get_invalid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get invalid datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_invalid_request(template_url=self.get_invalid.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/datetimerfc1123/invalid"}  # type: ignore

    @distributed_trace
    def get_overflow(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get overflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_overflow_request(template_url=self.get_overflow.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow.metadata = {"url": "/datetimerfc1123/overflow"}  # type: ignore

    @distributed_trace
    def get_underflow(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get underflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_underflow_request(template_url=self.get_underflow.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow.metadata = {"url": "/datetimerfc1123/underflow"}  # type: ignore

    @distributed_trace
    def put_utc_max_date_time(
        self,
        datetime_body,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put max datetime value Fri, 31 Dec 9999 23:59:59 GMT.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(datetime_body, "rfc-1123")
        content = json.dumps(content)

        request = build_put_utc_max_date_time_request(
            content=content,
            content_type=content_type,
            template_url=self.put_utc_max_date_time.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_utc_max_date_time.metadata = {"url": "/datetimerfc1123/max"}  # type: ignore

    @distributed_trace
    def get_utc_lowercase_max_date_time(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get max datetime value fri, 31 dec 9999 23:59:59 gmt.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_utc_lowercase_max_date_time_request(
            template_url=self.get_utc_lowercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_lowercase_max_date_time.metadata = {"url": "/datetimerfc1123/max/lowercase"}  # type: ignore

    @distributed_trace
    def get_utc_uppercase_max_date_time(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get max datetime value FRI, 31 DEC 9999 23:59:59 GMT.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_utc_uppercase_max_date_time_request(
            template_url=self.get_utc_uppercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_uppercase_max_date_time.metadata = {"url": "/datetimerfc1123/max/uppercase"}  # type: ignore

    @distributed_trace
    def put_utc_min_date_time(
        self,
        datetime_body,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(datetime_body, "rfc-1123")
        content = json.dumps(content)

        request = build_put_utc_min_date_time_request(
            content=content,
            content_type=content_type,
            template_url=self.put_utc_min_date_time.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_utc_min_date_time.metadata = {"url": "/datetimerfc1123/min"}  # type: ignore

    @distributed_trace
    def get_utc_min_date_time(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_utc_min_date_time_request(template_url=self.get_utc_min_date_time.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("rfc-1123", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_min_date_time.metadata = {"url": "/datetimerfc1123/min"}  # type: ignore
