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
from ...rest import inheritance as rest_inheritance

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class InheritanceOperations:
    """InheritanceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
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
    async def get_valid(self, **kwargs: Any) -> "_models.Siamese":
        """Get complex types that extend others.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Siamese, or the result of cls(response)
        :rtype: ~bodycomplex.models.Siamese
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Siamese"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_inheritance.build_get_valid_request(
            template_url=self.get_valid.metadata["url"], **kwargs
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

        deserialized = self._deserialize("Siamese", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore

    @distributed_trace_async
    async def put_valid(self, complex_body: "_models.Siamese", **kwargs: Any) -> None:
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green,
         breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
         the 2nd one named "Tomato" with id=-1 and food="french fries".
        :type complex_body: ~bodycomplex.models.Siamese
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(complex_body, "Siamese")

        request = rest_inheritance.build_put_valid_request(
            content_type=content_type, json=json, template_url=self.put_valid.metadata["url"], **kwargs
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

    put_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore
