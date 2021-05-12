# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from my.library.aio import AsyncCustomDefaultPollingMethod, AsyncCustomPager, AsyncCustomPoller

from ... import models as _models
from ..._rest import *

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PollingPagingExampleOperationsMixin:

    async def _basic_poll_initial(
        self,
        product: Optional["_models.Product"] = None,
        **kwargs: Any
    ) -> Optional["_models.Product"]:
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Product"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        if product is not None:
            product = self._serialize.body(product, 'Product')

        request = prepare_basic_polling_initial(
            product=product,
            template_url=self._basic_poll_initial.metadata['url'],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _basic_poll_initial.metadata = {'url': '/basic/polling'}  # type: ignore

    async def begin_basic_polling(
        self,
        product: Optional["_models.Product"] = None,
        **kwargs: Any
    ) -> AsyncCustomPoller["_models.Product"]:
        """A simple polling operation.

        :param product: Product to put.
        :type product: ~azure.directives.sample.models.Product
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
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._basic_poll_initial(
                product=product,


                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Product', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncCustomDefaultPollingMethod(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncCustomPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncCustomPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_basic_polling.metadata = {'url': '/basic/polling'}  # type: ignore


    def basic_paging(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.ProductResult"]:
        """A simple paging operation.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~my.library.aio.AsyncCustomPager[~azure.directives.sample.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProductResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            if not next_link:
                request = prepare_basic_paging(
                    template_url=self.basic_paging.metadata['url'],
                    **kwargs
                )
                request.url = self._client.format_url(request.url)
                kwargs.pop("content_type", None)
            else:
                request = prepare_basic_paging(
                    template_url=self.basic_paging.metadata['url'],
                    **kwargs
                )
                request.url = self._client.format_url(request.url)
                kwargs.pop("content_type", None)
                # little hacky, but this code will soon be replaced with code that won't need the hack
                request._internal_request.method = "GET"
                request.url = self._client.format_url(next_link)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncCustomPager(
            get_next, extract_data
        )
    basic_paging.metadata = {'url': '/basic/paging'}  # type: ignore
