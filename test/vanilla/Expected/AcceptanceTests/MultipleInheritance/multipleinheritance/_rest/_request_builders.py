# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()


def build_get_horse_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a horse with name 'Fred' and isAShowHorse true.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/horse")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_horse_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a horse with name 'General' and isAShowHorse false.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Put a horse with name 'General' and isAShowHorse false.
    :paramtype json: Any
    :keyword content: Put a horse with name 'General' and isAShowHorse false.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "isAShowHorse": "bool (optional)",
                "name": "str"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/horse")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_pet_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a pet with name 'Peanut'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/pet")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_pet_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a pet with name 'Butter'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Put a pet with name 'Butter'.
    :paramtype json: Any
    :keyword content: Put a pet with name 'Butter'.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "name": "str"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/pet")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_feline_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a feline where meows and hisses are true.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/feline")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_feline_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a feline who hisses and doesn't meow.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Put a feline who hisses and doesn't meow.
    :paramtype json: Any
    :keyword content: Put a feline who hisses and doesn't meow.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "hisses": "bool (optional)",
                "meows": "bool (optional)"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/feline")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_cat_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a cat with name 'Whiskers' where likesMilk, meows, and hisses is true.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/cat")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_cat_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.
    :paramtype json: Any
    :keyword content: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is
     true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "hisses": "bool (optional)",
                "likesMilk": "bool (optional)",
                "meows": "bool (optional)",
                "name": "str"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/cat")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_kitten_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a kitten with name 'Gatito' where likesMilk and meows is true, and hisses and eatsMiceYet
    is false.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/kitten")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_kitten_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
    true.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
     eatsMiceYet is true.
    :paramtype json: Any
    :keyword content: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
     eatsMiceYet is true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "eatsMiceYet": "bool (optional)",
                "hisses": "bool (optional)",
                "likesMilk": "bool (optional)",
                "meows": "bool (optional)",
                "name": "str"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/multipleInheritance/kitten")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)
