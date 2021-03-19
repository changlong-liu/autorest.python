# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_implicit_get_required_path
    from ._preparers_py3 import prepare_implicit_put_optional_query
    from ._preparers_py3 import prepare_implicit_put_optional_header
    from ._preparers_py3 import prepare_implicit_put_optional_body
    from ._preparers_py3 import prepare_implicit_put_optional_binary_body
    from ._preparers_py3 import prepare_implicit_get_required_global_path
    from ._preparers_py3 import prepare_implicit_get_required_global_query
    from ._preparers_py3 import prepare_implicit_get_optional_global_query
    from ._preparers_py3 import prepare_explicit_put_optional_binary_body
    from ._preparers_py3 import prepare_explicit_put_required_binary_body
    from ._preparers_py3 import prepare_explicit_post_required_integer_parameter
    from ._preparers_py3 import prepare_explicit_post_optional_integer_parameter
    from ._preparers_py3 import prepare_explicit_post_required_integer_property
    from ._preparers_py3 import prepare_explicit_post_optional_integer_property
    from ._preparers_py3 import prepare_explicit_post_required_integer_header
    from ._preparers_py3 import prepare_explicit_post_optional_integer_header
    from ._preparers_py3 import prepare_explicit_post_required_string_parameter
    from ._preparers_py3 import prepare_explicit_post_optional_string_parameter
    from ._preparers_py3 import prepare_explicit_post_required_string_property
    from ._preparers_py3 import prepare_explicit_post_optional_string_property
    from ._preparers_py3 import prepare_explicit_post_required_string_header
    from ._preparers_py3 import prepare_explicit_post_optional_string_header
    from ._preparers_py3 import prepare_explicit_post_required_class_parameter
    from ._preparers_py3 import prepare_explicit_post_optional_class_parameter
    from ._preparers_py3 import prepare_explicit_post_required_class_property
    from ._preparers_py3 import prepare_explicit_post_optional_class_property
    from ._preparers_py3 import prepare_explicit_post_required_array_parameter
    from ._preparers_py3 import prepare_explicit_post_optional_array_parameter
    from ._preparers_py3 import prepare_explicit_post_required_array_property
    from ._preparers_py3 import prepare_explicit_post_optional_array_property
    from ._preparers_py3 import prepare_explicit_post_required_array_header
    from ._preparers_py3 import prepare_explicit_post_optional_array_header
except (SyntaxError, ImportError):
    from ._preparers import prepare_implicit_get_required_path  # type: ignore
    from ._preparers import prepare_implicit_put_optional_query  # type: ignore
    from ._preparers import prepare_implicit_put_optional_header  # type: ignore
    from ._preparers import prepare_implicit_put_optional_body  # type: ignore
    from ._preparers import prepare_implicit_put_optional_binary_body  # type: ignore
    from ._preparers import prepare_implicit_get_required_global_path  # type: ignore
    from ._preparers import prepare_implicit_get_required_global_query  # type: ignore
    from ._preparers import prepare_implicit_get_optional_global_query  # type: ignore
    from ._preparers import prepare_explicit_put_optional_binary_body  # type: ignore
    from ._preparers import prepare_explicit_put_required_binary_body  # type: ignore
    from ._preparers import prepare_explicit_post_required_integer_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_optional_integer_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_required_integer_property  # type: ignore
    from ._preparers import prepare_explicit_post_optional_integer_property  # type: ignore
    from ._preparers import prepare_explicit_post_required_integer_header  # type: ignore
    from ._preparers import prepare_explicit_post_optional_integer_header  # type: ignore
    from ._preparers import prepare_explicit_post_required_string_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_optional_string_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_required_string_property  # type: ignore
    from ._preparers import prepare_explicit_post_optional_string_property  # type: ignore
    from ._preparers import prepare_explicit_post_required_string_header  # type: ignore
    from ._preparers import prepare_explicit_post_optional_string_header  # type: ignore
    from ._preparers import prepare_explicit_post_required_class_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_optional_class_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_required_class_property  # type: ignore
    from ._preparers import prepare_explicit_post_optional_class_property  # type: ignore
    from ._preparers import prepare_explicit_post_required_array_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_optional_array_parameter  # type: ignore
    from ._preparers import prepare_explicit_post_required_array_property  # type: ignore
    from ._preparers import prepare_explicit_post_optional_array_property  # type: ignore
    from ._preparers import prepare_explicit_post_required_array_header  # type: ignore
    from ._preparers import prepare_explicit_post_optional_array_header  # type: ignore

__all__ = [
    "prepare_implicit_get_required_path",
    "prepare_implicit_put_optional_query",
    "prepare_implicit_put_optional_header",
    "prepare_implicit_put_optional_body",
    "prepare_implicit_put_optional_binary_body",
    "prepare_implicit_get_required_global_path",
    "prepare_implicit_get_required_global_query",
    "prepare_implicit_get_optional_global_query",
    "prepare_explicit_put_optional_binary_body",
    "prepare_explicit_put_required_binary_body",
    "prepare_explicit_post_required_integer_parameter",
    "prepare_explicit_post_optional_integer_parameter",
    "prepare_explicit_post_required_integer_property",
    "prepare_explicit_post_optional_integer_property",
    "prepare_explicit_post_required_integer_header",
    "prepare_explicit_post_optional_integer_header",
    "prepare_explicit_post_required_string_parameter",
    "prepare_explicit_post_optional_string_parameter",
    "prepare_explicit_post_required_string_property",
    "prepare_explicit_post_optional_string_property",
    "prepare_explicit_post_required_string_header",
    "prepare_explicit_post_optional_string_header",
    "prepare_explicit_post_required_class_parameter",
    "prepare_explicit_post_optional_class_parameter",
    "prepare_explicit_post_required_class_property",
    "prepare_explicit_post_optional_class_property",
    "prepare_explicit_post_required_array_parameter",
    "prepare_explicit_post_optional_array_parameter",
    "prepare_explicit_post_required_array_property",
    "prepare_explicit_post_optional_array_property",
    "prepare_explicit_post_required_array_header",
    "prepare_explicit_post_optional_array_header",
]
