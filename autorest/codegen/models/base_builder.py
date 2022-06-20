# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from abc import abstractmethod
from typing import (
    Any,
    Dict,
    List,
    Optional,
    TypeVar,
    Union,
    TYPE_CHECKING,
    Generic,
)
from .base_model import BaseModel
from .parameter_list import (
    ParameterList,
    RequestBuilderParameterList,
    OverloadedRequestBuilderParameterList,
)
from .base_type import BaseType
from .constant_type import ConstantType
from .parameter import ParameterLocation

ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[
        ParameterList,
        RequestBuilderParameterList,
        OverloadedRequestBuilderParameterList,
    ],
)


if TYPE_CHECKING:
    from .code_model import CodeModel
    from .operation import Operation
    from .request_builder import RequestBuilder

_LOGGER = logging.getLogger(__name__)


class BaseBuilder(Generic[ParameterListType], BaseModel):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters: ParameterListType,
        *,
        overloads=None,
        want_tracing: bool = True,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self._description: str = yaml_data.get("description", "")
        self.parameters = parameters
        self.overloads: Union[List["Operation"], List["RequestBuilder"]] = (
            overloads or []
        )
        self._summary: str = yaml_data.get("summary", "")
        self.want_tracing = want_tracing
        self.group_name: str = yaml_data["groupName"]
        self.is_overload: bool = yaml_data["isOverload"]
        self.api_versions: List[str] = yaml_data["apiVersions"]

        if code_model.options["version_tolerant"] and yaml_data.get("abstract"):
            _LOGGER.warning(
                'Not going to generate operation "%s" because we are unable to generate this '
                "type of operation right now. "
                'Please write your own custom operation in the "_patch.py" file '
                "following https://aka.ms/azsdk/python/dpcodegen/python/customize",
                name,
            )
            self.abstract = True
        else:
            self.abstract = False

    @property
    def summary(self) -> Optional[str]:
        if self.abstract:
            return None
        return self._summary

    @property
    def pylint_disable(self) -> str:
        return ""

    @abstractmethod
    def response_type_annotation(self, **kwargs) -> str:
        ...

    @abstractmethod
    def response_docstring_text(self, **kwargs) -> str:
        ...

    @abstractmethod
    def response_docstring_type(self, **kwargs) -> str:
        ...

    @property
    def description(self) -> str:
        if self.abstract:
            return (
                f'You need to write a custom operation for "{self.name}". Please refer to '
                "https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
            )
        return self._description or self.name

    def method_signature(self, async_mode: bool) -> List[str]:
        if self.abstract:
            return ["*args,", "**kwargs"]
        return self.parameters.method_signature(
            async_mode, use_default_type=not self.is_overload
        )

    @property
    def default_type_annotations(
        self,
    ) -> Dict[str, str]:  # return a dict of type_annotation --> default_type_annotation
        if self.abstract or self.is_overload or self.code_model.is_legacy:
            return {}
        return {
            p.type.type_annotation(): p.type.default_type_annotation
            for p in self.parameters.keyword_only
            if (p.client_default_value is not None or p.optional)
            and not isinstance(p.type, ConstantType)
            and (p.location in [ParameterLocation.HEADER, ParameterLocation.QUERY])
        }
