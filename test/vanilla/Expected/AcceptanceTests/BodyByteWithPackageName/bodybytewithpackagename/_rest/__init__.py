# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_byte_get_null
    from ._preparers_py3 import prepare_byte_get_empty
    from ._preparers_py3 import prepare_byte_get_non_ascii
    from ._preparers_py3 import prepare_byte_put_non_ascii
    from ._preparers_py3 import prepare_byte_get_invalid
except (SyntaxError, ImportError):
    from ._preparers import prepare_byte_get_null  # type: ignore
    from ._preparers import prepare_byte_get_empty  # type: ignore
    from ._preparers import prepare_byte_get_non_ascii  # type: ignore
    from ._preparers import prepare_byte_put_non_ascii  # type: ignore
    from ._preparers import prepare_byte_get_invalid  # type: ignore

__all__ = [
    "prepare_byte_get_null",
    "prepare_byte_get_empty",
    "prepare_byte_get_non_ascii",
    "prepare_byte_put_non_ascii",
    "prepare_byte_get_invalid",
]
