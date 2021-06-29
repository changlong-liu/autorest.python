# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
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
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest as PipelineTransportHttpRequest
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ...rest import path_items as rest_path_items

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PathItemsOperations:
    """PathItemsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~url.models
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

    @distributed_trace_async
    async def get_all_with_values(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_path_items.build_get_all_with_values_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_all_with_values.metadata["url"],
            **kwargs
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_all_with_values.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery"}  # type: ignore

    @distributed_trace_async
    async def get_global_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_path_items.build_get_global_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_query_null.metadata["url"],
            **kwargs
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery"}  # type: ignore

    @distributed_trace_async
    async def get_global_and_local_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain null value.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_path_items.build_get_global_and_local_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_and_local_query_null.metadata["url"],
            **kwargs
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_and_local_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null"}  # type: ignore

    @distributed_trace_async
    async def get_local_path_item_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery=null, localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: should contain value null.
        :type path_item_string_query: str
        :param local_string_query: should contain value null.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_path_items.build_get_local_path_item_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_local_path_item_query_null.metadata["url"],
            **kwargs
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_local_path_item_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null"}  # type: ignore
