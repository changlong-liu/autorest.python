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

from typing import Any, Optional, TYPE_CHECKING

from azure.core import PipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import MultiapiServiceClientConfiguration
from ._operations_mixin import MultiapiServiceClientOperationsMixin
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class MultiapiServiceClient(MultiapiServiceClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """Service client for multiapi client testing.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '1.0.0'
    _PROFILE_TAG = "multiapisecurity.MultiapiServiceClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        api_version=None, # type: Optional[str]
        base_url: str = "http://localhost:3000",
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MultiapiServiceClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 0.0.0: :mod:`v0.models<multiapisecurity.v0.models>`
           * 1.0.0: :mod:`v1.models<multiapisecurity.v1.models>`
        """
        if api_version == '0.0.0':
            from .v0 import models
            return models
        elif api_version == '1.0.0':
            from .v1 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def operation_group_one(self):
        """Instance depends on the API version:

           * 0.0.0: :class:`OperationGroupOneOperations<multiapisecurity.v0.operations.OperationGroupOneOperations>`
           * 1.0.0: :class:`OperationGroupOneOperations<multiapisecurity.v1.operations.OperationGroupOneOperations>`
        """
        api_version = self._get_api_version('operation_group_one')
        if api_version == '0.0.0':
            from .v0.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '1.0.0':
            from .v1.operations import OperationGroupOneOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_group_one'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
