# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

import msrest.serialization


class MyException(msrest.serialization.Model):
    """MyException.

    :ivar status_code:
    :vartype status_code: str
    """

    _attribute_map = {
        "status_code": {"key": "statusCode", "type": "str"},
    }

    def __init__(self, *, status_code: Optional[str] = None, **kwargs):
        """
        :keyword status_code:
        :paramtype status_code: str
        """
        super().__init__(**kwargs)
        self.status_code = status_code


class B(MyException):
    """B.

    :ivar status_code:
    :vartype status_code: str
    :ivar text_status_code:
    :vartype text_status_code: str
    """

    _attribute_map = {
        "status_code": {"key": "statusCode", "type": "str"},
        "text_status_code": {"key": "textStatusCode", "type": "str"},
    }

    def __init__(self, *, status_code: Optional[str] = None, text_status_code: Optional[str] = None, **kwargs):
        """
        :keyword status_code:
        :paramtype status_code: str
        :keyword text_status_code:
        :paramtype text_status_code: str
        """
        super().__init__(status_code=status_code, **kwargs)
        self.text_status_code = text_status_code


class C(msrest.serialization.Model):
    """C.

    :ivar http_code:
    :vartype http_code: str
    """

    _attribute_map = {
        "http_code": {"key": "httpCode", "type": "str"},
    }

    def __init__(self, *, http_code: Optional[str] = None, **kwargs):
        """
        :keyword http_code:
        :paramtype http_code: str
        """
        super().__init__(**kwargs)
        self.http_code = http_code


class D(msrest.serialization.Model):
    """D.

    :ivar http_status_code:
    :vartype http_status_code: str
    """

    _attribute_map = {
        "http_status_code": {"key": "httpStatusCode", "type": "str"},
    }

    def __init__(self, *, http_status_code: Optional[str] = None, **kwargs):
        """
        :keyword http_status_code:
        :paramtype http_status_code: str
        """
        super().__init__(**kwargs)
        self.http_status_code = http_status_code


class Error(msrest.serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message
