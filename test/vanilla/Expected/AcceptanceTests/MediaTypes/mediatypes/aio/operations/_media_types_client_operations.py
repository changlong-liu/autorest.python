# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MediaTypesClientOperationsMixin:
    def _analyze_body_request(self, body: Optional[Union[IO, "_models.SourcePath"]] = None, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/mediatypes/analyze")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if header_parameters["Content-Type"].split(";")[0] in [
            "application/pdf",
            "image/jpeg",
            "image/png",
            "image/tiff",
        ]:
            body_content_kwargs["stream_content"] = body

        elif header_parameters["Content-Type"].split(";")[0] in ["application/json"]:
            body_content_kwargs["content"] = body
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(
                    header_parameters["Content-Type"]
                )
            )
        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace_async
    async def analyze_body(self, input: Optional[Union[IO, "_models.SourcePath"]] = None, **kwargs) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter.
        :type input: IO or ~mediatypes.models.SourcePath
        :keyword str content_type: Media type of the body sent to the API. Default value is "application/json".
         Allowed values are: "application/pdf", "image/jpeg", "image/png", "image/tiff", "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.get("content_type", "application/json")
        request = self._analyze_body_request(body=input, template_url=self.analyze_body.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_body.metadata = {"url": "/mediatypes/analyze"}  # type: ignore

    def _content_type_with_encoding_request(self, body: Optional[str] = None, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "text/plain")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", "/mediatypes/contentTypeWithEncoding")

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["content"] = body
        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    @distributed_trace_async
    async def content_type_with_encoding(self, input: Optional[str] = None, **kwargs) -> str:
        """Pass in contentType 'text/plain; encoding=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter.
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if input is not None:
            input = self._serialize.body(input, "str")

        request = self._content_type_with_encoding_request(
            body=input, template_url=self.content_type_with_encoding.metadata["url"], **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    content_type_with_encoding.metadata = {"url": "/mediatypes/contentTypeWithEncoding"}  # type: ignore
