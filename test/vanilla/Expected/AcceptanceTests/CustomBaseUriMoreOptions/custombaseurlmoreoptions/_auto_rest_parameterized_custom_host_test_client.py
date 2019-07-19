# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from azure.core.exceptions import map_error
from .operations import PathsOperations
from . import models


class AutoRestParameterizedCustomHostTestClient(object):
    """Test Infrastructure for AutoRest


    :ivar paths: Paths operations
    :vartype paths: custombaseurlmoreoptions.operations.PathsOperations

    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the
     parameterized host. Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(self, subscription_id, dns_suffix, **kwargs):

        base_url = '{vault}{secret}{dnsSuffix}'
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(subscription_id, dns_suffix, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
