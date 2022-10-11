# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_no_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[Literal["value1"]] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_default_request(
    *, input: Literal["value1"] = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_no_default_request(**kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    input = kwargs.pop("input", _params.pop("input", "value1"))  # type: Literal["value1"]
    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_default_request(**kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    input = kwargs.pop("input", _params.pop("input", "value1"))  # type: Literal["value1"]
    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_required_one_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_model_as_string_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/constants/putModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, **kwargs)


def build_contants_put_client_constants_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    header_constant = kwargs.pop("header_constant", _headers.pop("header-constant", True))  # type: Literal[True]
    query_constant = kwargs.pop("query_constant", _params.pop("query-constant", 100))  # type: Literal[100]
    path_constant = kwargs.pop("path_constant", "path")  # type: Literal["path"]
    # Construct URL
    _url = "/constants/clientConstants/{path-constant}"
    path_format_arguments = {
        "path-constant": _SERIALIZER.url("path_constant", path_constant, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["query-constant"] = _SERIALIZER.query("query_constant", query_constant, "int")

    # Construct headers
    _headers["header-constant"] = _SERIALIZER.header("header_constant", header_constant, "bool")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class ContantsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~constantsversiontolerant.AutoRestSwaggerConstantService`'s
        :attr:`contants` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is None.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_no_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[Literal["value1"]] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are "value1" and None. Default value is None.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Literal["value1"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are "value1" and None. Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_no_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Required.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Default value is "value1". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input = kwargs.pop("input", _params.pop("input", "value1"))  # type: Literal["value1"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Default value is "value1". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input = kwargs.pop("input", _params.pop("input", "value1"))  # type: Literal["value1"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_no_model_as_string_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is None.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_no_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_no_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1" Default value is None.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_no_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1" Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_no_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Required.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Known values are: "value1" and "value2". Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1" Required.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1" Default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_model_as_string_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_client_constants(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Pass constants from the client to this function. Will pass in constant path, query, and header
        parameters.

        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_contants_put_client_constants_request(
            header_constant=self._config.header_constant,
            query_constant=self._config.query_constant,
            path_constant=self._config.path_constant,
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

        if cls:
            return cls(pipeline_response, None, {})
