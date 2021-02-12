# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class BoolOperations(object):
    """BoolOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyboolean.models
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

    def _get_true_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/true")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace
    def get_true(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get true Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_true_request(template_url=self.get_true.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_true.metadata = {"url": "/bool/true"}  # type: ignore

    def _put_true_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        body = True
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/true")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body = self._serialize.body(body, "bool")

        body_content_kwargs["content"] = body
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace
    def put_true(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set Boolean value true.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_true_request(template_url=self.put_true.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_true.metadata = {"url": "/bool/true"}  # type: ignore

    def _get_false_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/false")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace
    def get_false(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get false Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_false_request(template_url=self.get_false.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_false.metadata = {"url": "/bool/false"}  # type: ignore

    def _put_false_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        body = False
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/false")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body = self._serialize.body(body, "bool")

        body_content_kwargs["content"] = body
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace
    def put_false(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set Boolean value false.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_false_request(template_url=self.put_false.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_false.metadata = {"url": "/bool/false"}  # type: ignore

    def _get_null_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/null")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[bool]
        """Get null Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or None, or the result of cls(response)
        :rtype: bool or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[bool]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_null_request(template_url=self.get_null.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/bool/null"}  # type: ignore

    def _get_invalid_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/bool/invalid")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace
    def get_invalid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get invalid Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_invalid_request(template_url=self.get_invalid.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/bool/invalid"}  # type: ignore
