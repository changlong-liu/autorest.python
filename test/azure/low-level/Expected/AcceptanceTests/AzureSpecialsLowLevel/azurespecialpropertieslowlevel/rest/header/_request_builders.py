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

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_custom_named_request_id_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/customNamedRequestId')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    header_parameters.update(kwargs.pop("headers", {}))

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_custom_named_request_id_param_grouping_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request,
    via a parameter group.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/customNamedRequestIdParamGrouping')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    header_parameters.update(kwargs.pop("headers", {}))

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_custom_named_request_id_head_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/customNamedRequestIdHead')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    header_parameters.update(kwargs.pop("headers", {}))

    return HttpRequest(
        method="HEAD",
        url=url,
        headers=header_parameters,
        **kwargs
    )
