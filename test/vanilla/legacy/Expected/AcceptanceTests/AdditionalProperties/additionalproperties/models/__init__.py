# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CatAPTrue
from ._models_py3 import Error
from ._models_py3 import PetAPInProperties
from ._models_py3 import PetAPInPropertiesWithAPString
from ._models_py3 import PetAPObject
from ._models_py3 import PetAPString
from ._models_py3 import PetAPTrue

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CatAPTrue",
    "Error",
    "PetAPInProperties",
    "PetAPInPropertiesWithAPString",
    "PetAPObject",
    "PetAPString",
    "PetAPTrue",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
