# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from ._configuration import AutoRestSwaggerConstantServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestSwaggerConstantService:
    """Test Infrastructure for AutoRest Swagger Constant.

    :keyword endpoint: Service URL. Default value is 'http://localhost:3000'.
    :paramtype endpoint: str
    :keyword header_constant: Constant header property on the client that is a required parameter
     for operation 'constants_putClientConstants'. The default value is True. Note that overriding
     this default value may result in unsupported behavior.
    :paramtype header_constant: bool
    :keyword query_constant: Constant query property on the client that is a required parameter for
     operation 'constants_putClientConstants'. The default value is 100. Note that overriding this
     default value may result in unsupported behavior.
    :paramtype query_constant: int
    :keyword path_constant: Constant path property on the client that is a required parameter for
     operation 'constants_putClientConstants'. The default value is "path". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype path_constant: str
    """

    def __init__(self, *, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        self._config = AutoRestSwaggerConstantServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `constantslowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from constantslowlevel.rest import contants
        >>> request = contants.build_put_no_model_as_string_no_required_two_value_no_default_request(input=input, **kwargs)
        <HttpRequest [PUT], url: '/constants/putNoModelAsStringNoRequiredTwoValueNoDefault'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestSwaggerConstantService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
