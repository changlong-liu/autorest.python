# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, TYPE_CHECKING

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

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/null")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/null")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/empty")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    json = kwargs.pop('json', "")  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/empty")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_get_mbcs_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/mbcs")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_mbcs_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    json = kwargs.pop('json', "啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€")  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/mbcs")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_get_whitespace_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/whitespace")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_whitespace_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    json = kwargs.pop('json', "    Now is the time for all good men to come to the aid of their country    ")  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/whitespace")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_get_not_provided_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/notProvided")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_base64_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/base64Encoding")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_base64_url_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/base64UrlEncoding")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_base64_url_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/base64UrlEncoding")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_null_base64_url_encoded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/string/nullBase64UrlEncoding")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class StringOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodystring.AutoRestSwaggerBATService`'s
        :attr:`string` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[str]
        """Get null string value value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or None or the result of cls(response)
        :rtype: str or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]

        request = build_get_null_request(
            template_url=self.get_null.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/string/null"}  # type: ignore

    @distributed_trace
    def put_null(  # pylint: disable=inconsistent-return-statements
        self,
        string_body=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value null.

        :param string_body: string body. Default value is None.
        :type string_body: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        if string_body is not None:
            _content = self._serialize.body(string_body, "str")
        else:
            _content = None

        request = build_put_null_request(
            content_type=content_type,
            content=_content,
            template_url=self.put_null.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_null.metadata = {"url": "/string/null"}  # type: ignore

    @distributed_trace
    def get_empty(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get empty string value value ''.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        request = build_get_empty_request(
            template_url=self.get_empty.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_empty.metadata = {"url": "/string/empty"}  # type: ignore

    @distributed_trace
    def put_empty(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value empty ''.

        :keyword string_body: string body. Required. Default value is "". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype string_body: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        string_body = kwargs.pop("string_body", "")  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(string_body, "str")

        request = build_put_empty_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_empty.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_empty.metadata = {"url": "/string/empty"}  # type: ignore

    @distributed_trace
    def get_mbcs(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get mbcs string value '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        request = build_get_mbcs_request(
            template_url=self.get_mbcs.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_mbcs.metadata = {"url": "/string/mbcs"}  # type: ignore

    @distributed_trace
    def put_mbcs(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value mbcs '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        :keyword string_body: string body. Default value is
         "啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype string_body: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        string_body = kwargs.pop(
            "string_body", "啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€"
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(string_body, "str")

        request = build_put_mbcs_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_mbcs.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_mbcs.metadata = {"url": "/string/mbcs"}  # type: ignore

    @distributed_trace
    def get_whitespace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get string value with leading and trailing whitespace
        ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid
        of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        request = build_get_whitespace_request(
            template_url=self.get_whitespace.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_whitespace.metadata = {"url": "/string/whitespace"}  # type: ignore

    @distributed_trace
    def put_whitespace(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set String value with leading and trailing whitespace
        ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid
        of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        :keyword string_body: string body. Default value is "    Now is the time for all good men to
         come to the aid of their country    ". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype string_body: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        string_body = kwargs.pop(
            "string_body", "    Now is the time for all good men to come to the aid of their country    "
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(string_body, "str")

        request = build_put_whitespace_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_whitespace.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_whitespace.metadata = {"url": "/string/whitespace"}  # type: ignore

    @distributed_trace
    def get_not_provided(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get String value when no string value is sent in response payload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        request = build_get_not_provided_request(
            template_url=self.get_not_provided.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_provided.metadata = {"url": "/string/notProvided"}  # type: ignore

    @distributed_trace
    def get_base64_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bytes
        """Get value that is base64 encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytes or the result of cls(response)
        :rtype: bytes
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[bytes]

        request = build_get_base64_encoded_request(
            template_url=self.get_base64_encoded.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bytearray", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_base64_encoded.metadata = {"url": "/string/base64Encoding"}  # type: ignore

    @distributed_trace
    def get_base64_url_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bytes
        """Get value that is base64url encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytes or the result of cls(response)
        :rtype: bytes
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[bytes]

        request = build_get_base64_url_encoded_request(
            template_url=self.get_base64_url_encoded.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("base64", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_base64_url_encoded.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    @distributed_trace
    def put_base64_url_encoded(  # pylint: disable=inconsistent-return-statements
        self,
        string_body,  # type: bytes
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put value that is base64url encoded.

        :param string_body: string body. Required.
        :type string_body: bytes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(string_body, "base64")

        request = build_put_base64_url_encoded_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_base64_url_encoded.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_base64_url_encoded.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    @distributed_trace
    def get_null_base64_url_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[bytes]
        """Get null value that is expected to be base64url encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytes or None or the result of cls(response)
        :rtype: bytes or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[bytes]]

        request = build_get_null_base64_url_encoded_request(
            template_url=self.get_null_base64_url_encoded.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("base64", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null_base64_url_encoded.metadata = {"url": "/string/nullBase64UrlEncoding"}  # type: ignore
