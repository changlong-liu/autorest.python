# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, cast, Dict, List, TypeVar

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .request_parameter import RequestParameter
from .request_parameter_list import RequestParameterList
from .schema_request import SchemaRequest
from .imports import FileImport
from .utils import get_converted_parameters


T = TypeVar('T')
OrderedSet = Dict[T, None]

def _non_binary_schema_media_types(media_types: List[str]) -> OrderedSet[str]:
    response_media_types: OrderedSet[str] = {}

    json_media_types = [media_type for media_type in media_types if "json" in media_type]
    xml_media_types = [media_type for media_type in media_types if "xml" in media_type]

    if not sorted(json_media_types + xml_media_types) == sorted(media_types):
        raise ValueError("The non-binary responses with schemas of {self.name} have incorrect json or xml mime types")
    if json_media_types:
        if "application/json" in json_media_types:
            response_media_types["application/json"] = None
        else:
            response_media_types[json_media_types[0]] = None
    if xml_media_types:
        if "application/xml" in xml_media_types:
            response_media_types["application/xml"] = None
        else:
            response_media_types[xml_media_types[0]] = None
    return response_media_types

class Request(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        url: str,
        method: str,
        multipart: bool,
        schema_requests: List[SchemaRequest],
        parameters: RequestParameterList,
        multiple_media_type_parameters: RequestParameterList,
    ):
        super(Request, self).__init__(yaml_data)
        self.name = name
        self.url = url
        self.method = method
        self.multipart = multipart
        self.schema_requests = schema_requests
        self.parameters = parameters
        self.multiple_media_type_parameters = multiple_media_type_parameters

    @property
    def content_type(self) -> str:
        return next(iter(
            [
                p.schema.get_declaration(cast(ConstantSchema, p.schema).value)
                for p in self.parameters.constant if p.serialized_name == "content_type"
            ]
        ))

    @property
    def is_stream(self) -> bool:
        """Is the request is a stream, like an upload."""
        return any(request.is_stream_request for request in self.schema_requests)

    @property
    def default_content_type(self) -> str:
        return next(
            p for p in self.parameters.constant if p.serialized_name == "content_type"
        ).constant_declaration

    @property
    def has_body_param_with_object_schema(self) -> bool:
        try:
            parameters = self.parameters.body + self.multiple_media_type_parameters.body
            return any([p for p in parameters if p.has_object_schema])
        except ValueError:
            return False

    @property
    def imports(self) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        if self.multiple_media_type_parameters:
            for parameter in self.multiple_media_type_parameters:
                file_import.merge(parameter.imports())
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Request":
        operation_name = yaml_data["language"]["python"]["name"]
        name = f"_{operation_name}_request"

        first_request = yaml_data["requests"][0]

        parameters, multiple_media_type_parameters = get_converted_parameters(yaml_data, RequestParameter.from_yaml)
        return cls(
            yaml_data=yaml_data,
            name=name,
            url=first_request["protocol"]["http"]["path"],
            method=first_request["protocol"]["http"]["method"],
            multipart=first_request["protocol"]["http"].get("multipart", False),
            schema_requests=[SchemaRequest.from_yaml(yaml) for yaml in yaml_data["requests"]],
            parameters=RequestParameterList(parameters),
            multiple_media_type_parameters=RequestParameterList(multiple_media_type_parameters),
        )
