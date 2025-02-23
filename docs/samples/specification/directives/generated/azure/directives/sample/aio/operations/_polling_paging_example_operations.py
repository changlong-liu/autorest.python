# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.async_paging import AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from my.library.aio import AsyncCustomDefaultPollingMethod, AsyncCustomPager, AsyncCustomPoller

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._polling_paging_example_operations import build_basic_paging_request, build_basic_polling_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PollingPagingExampleOperationsMixin:

    async def _basic_polling_initial(
        self,
        product: Optional[Union[_models.Product, IO]] = None,
        **kwargs: Any
    ) -> Optional[_models.Product]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.Product]]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IO, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, 'Product')
            else:
                _json = None

        request = build_basic_polling_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._basic_polling_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _basic_polling_initial.metadata = {'url': "/basic/polling"}  # type: ignore


    @overload
    async def begin_basic_polling(
        self,
        product: Optional[_models.Product] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncCustomPoller[_models.Product]:
        """A simple polling operation.

        :param product: Product to put. Default value is None.
        :type product: ~azure.directives.sample.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns either Product or the result of
         cls(response)
        :rtype: ~my.library.aio.AsyncCustomPoller[~azure.directives.sample.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_basic_polling(
        self,
        product: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncCustomPoller[_models.Product]:
        """A simple polling operation.

        :param product: Product to put. Default value is None.
        :type product: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns either Product or the result of
         cls(response)
        :rtype: ~my.library.aio.AsyncCustomPoller[~azure.directives.sample.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace_async
    async def begin_basic_polling(
        self,
        product: Optional[Union[_models.Product, IO]] = None,
        **kwargs: Any
    ) -> AsyncCustomPoller[_models.Product]:
        """A simple polling operation.

        :param product: Product to put. Is either a model type or a IO type. Default value is None.
        :type product: ~azure.directives.sample.models.Product or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns either Product or the result of
         cls(response)
        :rtype: ~my.library.aio.AsyncCustomPoller[~azure.directives.sample.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.Product]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._basic_polling_initial(  # type: ignore
                product=product,
                content_type=content_type,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Product', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncCustomDefaultPollingMethod(
                lro_delay,
                
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncCustomPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncCustomPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_basic_polling.metadata = {'url': "/basic/polling"}  # type: ignore

    @distributed_trace
    def basic_paging(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.Product"]:
        """A simple paging operation.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Product or the result of cls(response)
        :rtype: ~my.library.aio.AsyncCustomPager[~azure.directives.sample.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ProductResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_basic_paging_request(
                    template_url=self.basic_paging.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_basic_paging_request(
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncCustomPager(
            get_next, extract_data
        )
    basic_paging.metadata = {'url': "/basic/paging"}  # type: ignore
