# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient

from . import models
from ._configuration import AutoRestComplexTestServiceConfiguration
from .operations import (
    ArrayOperations,
    BasicOperations,
    DictionaryOperations,
    FlattencomplexOperations,
    InheritanceOperations,
    PolymorphicrecursiveOperations,
    PolymorphismOperations,
    PrimitiveOperations,
    ReadonlypropertyOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.rest import HttpRequest, HttpResponse


class AutoRestComplexTestService(
    object
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar basic: BasicOperations operations
    :vartype basic: bodycomplex.operations.BasicOperations
    :ivar primitive: PrimitiveOperations operations
    :vartype primitive: bodycomplex.operations.PrimitiveOperations
    :ivar array: ArrayOperations operations
    :vartype array: bodycomplex.operations.ArrayOperations
    :ivar dictionary: DictionaryOperations operations
    :vartype dictionary: bodycomplex.operations.DictionaryOperations
    :ivar inheritance: InheritanceOperations operations
    :vartype inheritance: bodycomplex.operations.InheritanceOperations
    :ivar polymorphism: PolymorphismOperations operations
    :vartype polymorphism: bodycomplex.operations.PolymorphismOperations
    :ivar polymorphicrecursive: PolymorphicrecursiveOperations operations
    :vartype polymorphicrecursive: bodycomplex.operations.PolymorphicrecursiveOperations
    :ivar readonlyproperty: ReadonlypropertyOperations operations
    :vartype readonlyproperty: bodycomplex.operations.ReadonlypropertyOperations
    :ivar flattencomplex: FlattencomplexOperations operations
    :vartype flattencomplex: bodycomplex.operations.FlattencomplexOperations
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2016-02-29". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        base_url="http://localhost:3000",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AutoRestComplexTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.basic = BasicOperations(self._client, self._config, self._serialize, self._deserialize)
        self.primitive = PrimitiveOperations(self._client, self._config, self._serialize, self._deserialize)
        self.array = ArrayOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dictionary = DictionaryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inheritance = InheritanceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphism = PolymorphismOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphicrecursive = PolymorphicrecursiveOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.readonlyproperty = ReadonlypropertyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.flattencomplex = FlattencomplexOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestComplexTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
