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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations import PathsOperations
from . import models


class AutoRestParameterizedHostTestClientConfiguration(AzureConfiguration):
    """Configuration for AutoRestParameterizedHostTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    """

    def __init__(
            self, credentials, host):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if host is None:
            raise ValueError("Parameter 'host' must not be None.")
        base_url = 'http://{accountName}{host}'

        super(AutoRestParameterizedHostTestClientConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestparameterizedhosttestclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.host = host


class AutoRestParameterizedHostTestClient(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestParameterizedHostTestClientConfiguration

    :ivar paths: Paths operations
    :vartype paths: custombaseurl.operations.PathsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    """

    def __init__(
            self, credentials, host):

        self.config = AutoRestParameterizedHostTestClientConfiguration(credentials, host)
        super(AutoRestParameterizedHostTestClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self.config, self._serialize, self._deserialize)
