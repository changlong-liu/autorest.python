# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AutoRestHeadExceptionTestServiceConfiguration
from .operations import HeadExceptionOperations


class AutoRestHeadExceptionTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar head_exception: HeadExceptionOperations operations
    :vartype head_exception: headexceptions.aio.operations.HeadExceptionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(self, credential: "AsyncTokenCredential", base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestHeadExceptionTestServiceConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {}  # type: Dict[str, Any]
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.head_exception = HeadExceptionOperations(self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `headexceptions.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from headexceptions.rest import prepare_headexception_head200
        >>> request = prepare_headexception_head200()
        <HttpRequest [HEAD], url: '/http/success/200'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        stream_response = kwargs.pop("stream_response", True)
        pipeline_response = await self._client._pipeline.run(request_copy, stream=stream_response, **kwargs)
        return AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestHeadExceptionTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
