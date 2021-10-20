# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()


def build_get_by_pet_id_request(pet_id: str, **kwargs: Any) -> HttpRequest:
    """get pet by id.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param pet_id: Pet id.
    :type pet_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/extensibleenums/pet/{petId}")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}))

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_add_pet_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """add pet.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. pet param.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). pet param.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }

            # response body for status code(s): 200
            response.json() == {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/extensibleenums/pet/addPet")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}))

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)
