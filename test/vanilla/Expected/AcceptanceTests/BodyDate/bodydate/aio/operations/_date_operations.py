# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DateOperations:
    """DateOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydate.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _get_null_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/null")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_null(self, **kwargs) -> Optional[datetime.date]:
        """Get null date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date or None, or the result of cls(response)
        :rtype: ~datetime.date or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[datetime.date]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_null_request(template_url=self.get_null.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/date/null"}  # type: ignore

    def _get_invalid_date_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/invaliddate")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_invalid_date(self, **kwargs) -> datetime.date:
        """Get invalid date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_invalid_date_request(template_url=self.get_invalid_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_date.metadata = {"url": "/date/invaliddate"}  # type: ignore

    def _get_overflow_date_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/overflowdate")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_overflow_date(self, **kwargs) -> datetime.date:
        """Get overflow date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_overflow_date_request(template_url=self.get_overflow_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow_date.metadata = {"url": "/date/overflowdate"}  # type: ignore

    def _get_underflow_date_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/underflowdate")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_underflow_date(self, **kwargs) -> datetime.date:
        """Get underflow date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_underflow_date_request(template_url=self.get_underflow_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow_date.metadata = {"url": "/date/underflowdate"}  # type: ignore

    def _put_max_date_request(self, body: datetime.date, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/max")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["content"] = body
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace_async
    async def put_max_date(self, date_body: datetime.date, **kwargs) -> None:
        """Put max date value 9999-12-31.

        :param date_body: date body.
        :type date_body: ~datetime.date
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        date_body = self._serialize.body(date_body, "date")

        request = self._put_max_date_request(body=date_body, template_url=self.put_max_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_max_date.metadata = {"url": "/date/max"}  # type: ignore

    def _get_max_date_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/max")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_max_date(self, **kwargs) -> datetime.date:
        """Get max date value 9999-12-31.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_max_date_request(template_url=self.get_max_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_max_date.metadata = {"url": "/date/max"}  # type: ignore

    def _put_min_date_request(self, body: datetime.date, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/min")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["content"] = body
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace_async
    async def put_min_date(self, date_body: datetime.date, **kwargs) -> None:
        """Put min date value 0000-01-01.

        :param date_body: date body.
        :type date_body: ~datetime.date
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        date_body = self._serialize.body(date_body, "date")

        request = self._put_min_date_request(body=date_body, template_url=self.put_min_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_min_date.metadata = {"url": "/date/min"}  # type: ignore

    def _get_min_date_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/date/min")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_min_date(self, **kwargs) -> datetime.date:
        """Get min date value 0000-01-01.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_min_date_request(template_url=self.get_min_date.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_min_date.metadata = {"url": "/date/min"}  # type: ignore
