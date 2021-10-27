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

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)


# fmt: off

def build_params_get_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    parameter1 = kwargs.pop('parameter1')  # type: str
    parameter2 = kwargs.pop('parameter2')  # type: str
    parameter3 = kwargs.pop('parameter3')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/llc/parameters')

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "parameter1"):
        query_parameters['parameter1'] = _SERIALIZER.query("parameter1", parameter1, 'str')
    if _param_not_set(query_parameters, "parameter2"):
        query_parameters['parameter2'] = _SERIALIZER.query("parameter2", parameter2, 'str')
    if _param_not_set(query_parameters, "parameter3"):
        query_parameters['parameter3'] = _SERIALIZER.query("parameter3", parameter3, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
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
class ParamsOperations(object):
    """ParamsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_required(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Any
        """Get true Boolean value on path.

        :keyword parameter1: I am a required parameter.
        :paramtype parameter1: str
        :keyword parameter2: I am a required parameter.
        :paramtype parameter2: str
        :keyword parameter3: I am a required parameter and I'm last in Swagger.
        :paramtype parameter3: str
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        parameter1 = kwargs.pop("parameter1")  # type: str
        parameter2 = kwargs.pop("parameter2")  # type: str
        parameter3 = kwargs.pop("parameter3")  # type: str

        request = build_params_get_required_request(
            parameter1=parameter1,
            parameter2=parameter2,
            parameter3=parameter3,
            template_url=self.get_required.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_required.metadata = {"url": "/llc/parameters"}  # type: ignore
