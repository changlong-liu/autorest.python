# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union, Set, Mapping


class ImportType(str, Enum):
    STDLIB = "stdlib"
    THIRDPARTY = "thirdparty"
    AZURECORE = "azurecore"
    LOCAL = "local"


class TypingSection(str, Enum):
    REGULAR = "regular"  # this import is always a typing import
    CONDITIONAL = "conditional"  # is a typing import when we're dealing with files that py2 will use, else regular
    TYPING = "typing"  # never a typing import


class ImportModel:
    def __init__(
        self,
        typing_section: TypingSection,
        import_type: ImportType,
        module_name: str,
        *,
        submodule_name: Optional[str] = None,
        alias: Optional[str] = None,
    ):
        self.typing_section = typing_section
        self.import_type = import_type
        self.module_name = module_name
        self.submodule_name = submodule_name
        self.alias = alias

    def __eq__(self, other):
        try:
            return (
                self.typing_section == other.typing_section
                and self.import_type == other.import_type
                and self.module_name == other.module_name
                and self.submodule_name == other.submodule_name
                and self.alias == other.alias
            )
        except AttributeError:
            return False

    def __hash__(self):
        retval: int = 0
        for attr in dir(self):
            if attr[0] != "_":
                retval += hash(getattr(self, attr))
        return retval


class TypeDefinition:
    def __init__(
        self,
        sync_definition: str,
        async_definition: str,
        version_imports: Mapping[Optional[Tuple[int, int]], ImportModel] = None,
    ):
        # version_imports: a map of "python version -> ImportModel".
        #                  The python version is in form of (major, minor), for instance (3, 9) stands for py3.9.
        #                  If the python version is None, it's a default ImportModel.
        self.sync_definition = sync_definition
        self.async_definition = async_definition
        self.version_imports = version_imports


class FileImport:
    def __init__(self, imports: List[ImportModel] = None) -> None:
        self.imports = imports or []
        # has sync and async type definitions
        self.type_definitions: Dict[str, TypeDefinition] = {}

    def _append_import(self, import_model: ImportModel) -> None:
        if not any(
            i
            for i in self.imports
            if all(
                getattr(i, attr) == getattr(import_model, attr)
                for attr in dir(i)
                if attr[0] != "_"
            )
        ):
            self.imports.append(import_model)

    def get_imports_from_section(
        self, typing_section: TypingSection
    ) -> List[ImportModel]:
        return [i for i in self.imports if i.typing_section == typing_section]

    def add_submodule_import(
        self,
        module_name: str,
        submodule_name: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR,
        alias: Optional[str] = None,
    ) -> None:
        """Add an import to this import block."""
        self._append_import(
            ImportModel(
                typing_section=typing_section,
                import_type=import_type,
                module_name=module_name,
                submodule_name=submodule_name,
                alias=alias,
            )
        )

    def add_import(
        self,
        module_name: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR,
        alias: Optional[str] = None,
    ) -> None:
        # Implementation detail: a regular import is just a "from" with no from
        self._append_import(
            ImportModel(
                typing_section=typing_section,
                import_type=import_type,
                module_name=module_name,
                alias=alias,
            )
        )

    def define_mypy_type(
        self,
        type_name: str,
        type_value: str,
        async_type_value: Optional[str] = None,
        version_imports: Mapping[Optional[Tuple[int, int]], ImportModel] = None,
    ):
        self.type_definitions[type_name] = TypeDefinition(
            type_value, async_type_value or type_value, version_imports
        )

    def merge(self, file_import: "FileImport") -> None:
        """Merge the given file import format."""
        for i in file_import.imports:
            self._append_import(i)
        self.type_definitions.update(file_import.type_definitions)

    def define_mutable_mapping_type(self) -> None:
        """Helper function for defining the mutable mapping type"""
        self.define_mypy_type(
            "JSON",
            "MutableMapping[str, Any] # pylint: disable=unsubscriptable-object",
            None,
            {
                (3, 9): ImportModel(
                    TypingSection.CONDITIONAL,
                    ImportType.STDLIB,
                    "collections.abc",
                    submodule_name="MutableMapping",
                ),
                None: ImportModel(
                    TypingSection.CONDITIONAL,
                    ImportType.STDLIB,
                    "typing",
                    submodule_name="MutableMapping",
                ),
            },
        )
        self.add_submodule_import("typing", "Any", ImportType.STDLIB)

    def to_dict(
        self,
    ) -> Dict[
        TypingSection,
        Dict[ImportType, Dict[str, Set[Optional[Union[str, Tuple[str, str]]]]]],
    ]:
        retval: Dict[
            TypingSection,
            Dict[ImportType, Dict[str, Set[Optional[Union[str, Tuple[str, str]]]]]],
        ] = dict()
        for i in self.imports:
            name_import: Optional[Union[str, Tuple[str, str]]] = None
            if i.submodule_name:
                name_import = (
                    (i.submodule_name, i.alias) if i.alias else i.submodule_name
                )
            retval.setdefault(i.typing_section, dict()).setdefault(
                i.import_type, dict()
            ).setdefault(i.module_name, set()).add(name_import)
        return retval
