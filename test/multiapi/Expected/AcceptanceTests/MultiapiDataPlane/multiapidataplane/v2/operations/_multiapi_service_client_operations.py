# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()

def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)

# fmt: off

def build_test_one_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    id = kwargs.pop('id')  # type: int
    message = kwargs.pop('message', None)  # type: Optional[str]

    api_version = "2.0.0"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "id"):
        query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if _param_not_set(query_parameters, "message") and message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    if _param_not_set(query_parameters, "api-version"):
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_test_different_calls_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    greeting_in_chinese = kwargs.pop('greeting_in_chinese', None)  # type: Optional[str]

    api_version = "2.0.0"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "greetinginenglish"):
        header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if _param_not_set(header_parameters, "greetinginchinese") and greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class MultiapiServiceClientOperationsMixin(object):

    @distributed_trace
    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ModelTwo"
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapidataplane.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ModelTwo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        
        request = build_test_one_request(
            id=id,
            message=message,
            template_url=self.test_one.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ModelTwo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore


    @distributed_trace
    def test_different_calls(
        self,
        greeting_in_english,  # type: str
        greeting_in_chinese=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test.
        :type greeting_in_chinese: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        
        request = build_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            greeting_in_chinese=greeting_in_chinese,
            template_url=self.test_different_calls.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

