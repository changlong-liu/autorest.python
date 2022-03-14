# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_head300_request(**kwargs: Any) -> HttpRequest:
    """Return 300 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/300"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=_url, headers=_headers, **kwargs)


def build_get300_request(**kwargs: Any) -> HttpRequest:
    """Return 300 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 300
            response.json() == [
                "str"  # Optional.
            ]
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/300"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_head301_request(**kwargs: Any) -> HttpRequest:
    """Return 301 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=_url, headers=_headers, **kwargs)


def build_get301_request(**kwargs: Any) -> HttpRequest:
    """Return 301 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put301_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put true Boolean value in request returns 301.  This request should not be automatically
    redirected, but should return the received 301 to the caller for evaluation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_head302_request(**kwargs: Any) -> HttpRequest:
    """Return 302 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=_url, headers=_headers, **kwargs)


def build_get302_request(**kwargs: Any) -> HttpRequest:
    """Return 302 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_patch302_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Patch true Boolean value in request returns 302.  This request should not be automatically
    redirected, but should return the received 302 to the caller for evaluation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_post303_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post true Boolean value in request returns 303.  This request should be automatically
    redirected usign a get, ultimately returning a 200 status code.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/303"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_head307_request(**kwargs: Any) -> HttpRequest:
    """Redirect with 307, resulting in a 200 success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=_url, headers=_headers, **kwargs)


def build_get307_request(**kwargs: Any) -> HttpRequest:
    """Redirect get with 307, resulting in a 200 success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_options307_request(**kwargs: Any) -> HttpRequest:
    """options redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="OPTIONS", url=_url, headers=_headers, **kwargs)


def build_put307_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_patch307_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Patch redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_post307_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_delete307_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Delete redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop(
        "content_type", case_insensitive_dict(_headers).pop("Content-Type", None)
    )  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop("{param.rest_api_name}", {param.constant_declaration})

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, headers=_headers, json=json, content=content, **kwargs)
