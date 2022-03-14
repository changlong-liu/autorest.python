# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._pets_operations import (
    build_create_ap_in_properties_request,
    build_create_ap_in_properties_with_ap_string_request,
    build_create_ap_object_request,
    build_create_ap_string_request,
    build_create_ap_true_request,
    build_create_cat_ap_true_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalproperties.aio.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: "_models.PetAPTrue", **kwargs: Any) -> "_models.PetAPTrue":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPTrue"]

        _json = self._serialize.body(create_parameters, "PetAPTrue")

        request = build_create_ap_true_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_ap_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_true.metadata = {"url": "/additionalProperties/true"}  # type: ignore

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: "_models.CatAPTrue", **kwargs: Any) -> "_models.CatAPTrue":
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CatAPTrue"]

        _json = self._serialize.body(create_parameters, "CatAPTrue")

        request = build_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_cat_ap_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CatAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_cat_ap_true.metadata = {"url": "/additionalProperties/true-subclass"}  # type: ignore

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: "_models.PetAPObject", **kwargs: Any) -> "_models.PetAPObject":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPObject"]

        _json = self._serialize.body(create_parameters, "PetAPObject")

        request = build_create_ap_object_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_ap_object.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPObject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_object.metadata = {"url": "/additionalProperties/type/object"}  # type: ignore

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: "_models.PetAPString", **kwargs: Any) -> "_models.PetAPString":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPString"]

        _json = self._serialize.body(create_parameters, "PetAPString")

        request = build_create_ap_string_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_ap_string.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_string.metadata = {"url": "/additionalProperties/type/string"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties(
        self, create_parameters: "_models.PetAPInProperties", **kwargs: Any
    ) -> "_models.PetAPInProperties":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPInProperties"]

        _json = self._serialize.body(create_parameters, "PetAPInProperties")

        request = build_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_ap_in_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties.metadata = {"url": "/additionalProperties/in/properties"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: "_models.PetAPInPropertiesWithAPString", **kwargs: Any
    ) -> "_models.PetAPInPropertiesWithAPString":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPInPropertiesWithAPString"]

        _json = self._serialize.body(create_parameters, "PetAPInPropertiesWithAPString")

        request = build_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            template_url=self.create_ap_in_properties_with_ap_string.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInPropertiesWithAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties_with_ap_string.metadata = {"url": "/additionalProperties/in/properties/with/additionalProperties/string"}  # type: ignore
