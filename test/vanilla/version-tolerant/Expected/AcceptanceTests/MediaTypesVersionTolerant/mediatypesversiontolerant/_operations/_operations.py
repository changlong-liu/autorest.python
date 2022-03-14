# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast

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

from .._vendor import MixinABC

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_analyze_body_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/mediatypes/analyze"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_analyze_body_no_accept_header_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    # Construct URL
    _url = "/mediatypes/analyzeNoAccept"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_content_type_with_encoding_request(*, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/mediatypes/contentTypeWithEncoding"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


def build_binary_body_with_two_content_types_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/mediatypes/binaryBodyTwoContentTypes"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_binary_body_with_three_content_types_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/mediatypes/binaryBodyThreeContentTypes"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_put_text_and_json_body_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/mediatypes/textAndJson"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


class MediaTypesClientOperationsMixin(MixinABC):
    @distributed_trace
    def analyze_body(
        self,
        input: Optional[Union[IO, JSONType]] = None,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Default value is None.
        :type input: IO or JSONType
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/pdf", "image/jpeg", "image/png", "image/tiff", and "application/json". Default
         value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                _json = input
        elif content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            _content = input
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
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

    @distributed_trace
    def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[IO, JSONType]] = None,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Default value is None.
        :type input: IO or JSONType
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/pdf", "image/jpeg", "image/png", "image/tiff", and "application/json". Default
         value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                _json = input
        elif content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            _content = input
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_no_accept_header_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def content_type_with_encoding(self, input: Optional[str] = None, **kwargs: Any) -> str:
        """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter. Default value is None.
        :type input: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", case_insensitive_dict(_headers).pop("Content-Type", "text/plain; charset=UTF-8")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _content = input

        request = build_content_type_with_encoding_request(
            content_type=content_type,
            content=_content,
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

    @distributed_trace
    def binary_body_with_two_content_types(
        self, message: Union[IO, JSONType], *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
        """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
        content type, and a byte stream of 'hello, world!' for application/octet-stream.

        :param message: The payload body.
        :type message: IO or JSONType
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "application/octet-stream". Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["application/octet-stream"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/json', 'application/octet-stream']".format(content_type)
            )

        request = build_binary_body_with_two_content_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
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

    @distributed_trace
    def binary_body_with_three_content_types(
        self, message: Union[IO, str], *, content_type: Optional[str] = "application/json", **kwargs: Any
    ) -> str:
        """Binary body with three content types. Pass in string 'hello, world' with content type
        'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
        'application/octet-stream'.

        :param message: The payload body.
        :type message: IO or str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json", "application/octet-stream", and "text/plain". Default value is
         "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["application/octet-stream", "text/plain"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/json', 'application/octet-stream', 'text/plain']".format(content_type)
            )

        request = build_binary_body_with_three_content_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
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

    @distributed_trace
    def put_text_and_json_body(
        self, message: Union[str, str], *, content_type: Optional[str] = "application/json", **kwargs: Any
    ) -> str:
        """Body that's either text/plain or application/json.

        :param message: The payload body.
        :type message: str or str
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "text/plain" or "application/json". Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["text/plain"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['text/plain', 'application/json']".format(content_type)
            )

        request = build_put_text_and_json_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
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
