# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_put_async_retry_succeeded_request_initial
    from ._request_builders_py3 import build_put201_creating_succeeded200_request_initial
    from ._request_builders_py3 import build_post202_retry200_request_initial
    from ._request_builders_py3 import build_post_async_retry_succeeded_request_initial
except (SyntaxError, ImportError):
    from ._request_builders import build_put_async_retry_succeeded_request_initial  # type: ignore
    from ._request_builders import build_put201_creating_succeeded200_request_initial  # type: ignore
    from ._request_builders import build_post202_retry200_request_initial  # type: ignore
    from ._request_builders import build_post_async_retry_succeeded_request_initial  # type: ignore

__all__ = [
    "build_put_async_retry_succeeded_request_initial",
    "build_put201_creating_succeeded200_request_initial",
    "build_post202_retry200_request_initial",
    "build_post_async_retry_succeeded_request_initial",
]
