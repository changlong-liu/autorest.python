# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from ...operations._operations import (
    build_paging_get_pages_partial_url_operation_next_request,
    build_paging_get_pages_partial_url_operation_request,
    build_paging_get_pages_partial_url_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PagingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~custombaseurlpagingversiontolerant.aio.AutoRestParameterizedHostTestPagingClient`'s
        :attr:`paging` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_pages_partial_url(self, account_name: str, **kwargs: Any) -> AsyncIterable[JSONType]:
        """A paging operation that combines custom url, paging and partial URL and expect to concat after
        host.

        :param account_name: Account Name.
        :type account_name: str
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[JSONType]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "nextLink": "str",  # Optional.
                    "values": [
                        {
                            "properties": {
                                "id": 0,  # Optional.
                                "name": "str"  # Optional.
                            }
                        }
                    ]
                }
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_paging_get_pages_partial_url_request(
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:

                request = build_paging_get_pages_partial_url_request(
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(next_link, **path_format_arguments)  # type: ignore

                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized["values"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def get_pages_partial_url_operation(self, account_name: str, **kwargs: Any) -> AsyncIterable[JSONType]:
        """A paging operation that combines custom url, paging and partial URL with next operation.

        :param account_name: Account Name.
        :type account_name: str
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[JSONType]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "nextLink": "str",  # Optional.
                    "values": [
                        {
                            "properties": {
                                "id": 0,  # Optional.
                                "name": "str"  # Optional.
                            }
                        }
                    ]
                }
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_paging_get_pages_partial_url_operation_request(
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:

                request = build_paging_get_pages_partial_url_operation_next_request(
                    next_link=next_link,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized["values"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
