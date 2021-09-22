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
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_no_default_request(**kwargs: Any) -> HttpRequest:
    input = "value1"
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_default_request(**kwargs: Any) -> HttpRequest:
    input = "value1"
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_required_one_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_model_as_string_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_contants_put_client_constants_request(**kwargs: Any) -> HttpRequest:
    header_constant = True
    query_constant = 100
    path_constant = "path"
    # Construct URL
    url = kwargs.pop("template_url", "/constants/clientConstants/{path-constant}")
    path_format_arguments = {
        "path-constant": _SERIALIZER.url("path_constant", path_constant, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["query-constant"] = _SERIALIZER.query("query_constant", query_constant, "int")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["header-constant"] = _SERIALIZER.header("header_constant", header_constant, "bool")

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **kwargs)


class ContantsOperations(object):
    """ContantsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_no_default(
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_two_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_no_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_default(
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_two_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_two_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_no_default(
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input:
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_one_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_no_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_default(
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input:
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_one_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_one_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredOneValueDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_required_two_value_no_default(self, *, input: str, **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_two_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_two_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_no_default.metadata = {"url": "/constants/putNoModelAsStringRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_required_two_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_two_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_two_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_default.metadata = {"url": "/constants/putNoModelAsStringRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_required_one_value_no_default(self, **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_one_value_no_default_request(
            template_url=self.put_no_model_as_string_required_one_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_no_default.metadata = {"url": "/constants/putNoModelAsStringRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_no_model_as_string_required_one_value_default(self, **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_one_value_default_request(
            template_url=self.put_no_model_as_string_required_one_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_default.metadata = {"url": "/constants/putNoModelAsStringRequiredOneValueDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_no_required_two_value_no_default(
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_two_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_two_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_no_default.metadata = {"url": "/constants/putModelAsStringNoRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_no_required_two_value_default(
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_two_value_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_two_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_default.metadata = {"url": "/constants/putModelAsStringNoRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_no_required_one_value_no_default(
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_one_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_one_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_no_default.metadata = {"url": "/constants/putModelAsStringNoRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_no_required_one_value_default(
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_one_value_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_one_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_default.metadata = {"url": "/constants/putModelAsStringNoRequiredOneValueDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_required_two_value_no_default(self, *, input: str, **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_two_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_required_two_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_no_default.metadata = {"url": "/constants/putModelAsStringRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_required_two_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_two_value_default_request(
            input=input,
            template_url=self.put_model_as_string_required_two_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_default.metadata = {"url": "/constants/putModelAsStringRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_required_one_value_no_default(self, *, input: str, **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_one_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_required_one_value_no_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_no_default.metadata = {"url": "/constants/putModelAsStringRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace
    def put_model_as_string_required_one_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_one_value_default_request(
            input=input,
            template_url=self.put_model_as_string_required_one_value_default.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_default.metadata = {"url": "/constants/putModelAsStringRequiredOneValueDefault"}  # type: ignore

    @distributed_trace
    def put_client_constants(self, **kwargs: Any) -> None:
        """Pass constants from the client to this function. Will pass in constant path, query, and header
        parameters.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_client_constants_request(
            template_url=self.put_client_constants.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_client_constants.metadata = {"url": "/constants/clientConstants/{path-constant}"}  # type: ignore
