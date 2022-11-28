# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import (
    ClassificationSchemaClientConfiguration,
    DataStreamClassificationsClientConfiguration,
    DataStreamClientConfiguration,
    DataStreamFilesClientConfiguration,
    DataStreamLogsContainerClientConfiguration,
    DataStreamStorageClientConfiguration,
    DataStreamTagsClientConfiguration,
    DiscoveryOperationsClientConfiguration,
    DiscoverySpecialFilesClientConfiguration,
    DiscoveryUploadsClientConfiguration,
    LongRunningOperationsClientConfiguration,
    MeasurementClientConfiguration,
    MeasurementMetadataClientConfiguration,
    MeasurementMetadataFileInfoClientConfiguration,
    MeasurementMetadataSchemaFileInfoClientConfiguration,
    MeasurementProcessingResultsClientConfiguration,
    MeasurementStateMachineClientConfiguration,
    UploadClientConfiguration,
    UploadDataFilesClientConfiguration,
    UploadMeasurementsClientConfiguration,
    UploadSpecialFilesClientConfiguration,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class LongRunningOperationsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: LongRunningOperationsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DiscoveryOperationsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DiscoveryOperationsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DiscoverySpecialFilesClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DiscoverySpecialFilesClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DiscoveryUploadsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DiscoveryUploadsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class UploadClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: UploadClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class UploadSpecialFilesClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: UploadSpecialFilesClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class UploadDataFilesClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: UploadDataFilesClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class UploadMeasurementsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: UploadMeasurementsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class ClassificationSchemaClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: ClassificationSchemaClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementMetadataClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementMetadataClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementProcessingResultsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementProcessingResultsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementStateMachineClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementStateMachineClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementMetadataFileInfoClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementMetadataFileInfoClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class MeasurementMetadataSchemaFileInfoClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MeasurementMetadataSchemaFileInfoClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamStorageClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamStorageClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamTagsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamTagsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamFilesClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamFilesClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamLogsContainerClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamLogsContainerClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class DataStreamClassificationsClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: DataStreamClassificationsClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
