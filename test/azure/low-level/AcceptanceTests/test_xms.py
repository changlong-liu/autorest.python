﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError

from azurespecialpropertieslowlevel import AutoRestAzureSpecialParametersTestClient
from azurespecialpropertieslowlevel.rest import xms_client_request_id, header

import pytest


@pytest.fixture
def client(credential, authentication_policy):
    valid_subscription = "1234-5678-9012-3456"
    with AutoRestAzureSpecialParametersTestClient(
        credential,
        valid_subscription,
        authentication_policy=authentication_policy,
    ) as client:
        yield client


@pytest.fixture
def client_no_request_id(credential, authentication_policy):
    valid_subscription = "1234-5678-9012-3456"
    with AutoRestAzureSpecialParametersTestClient(
        credential,
        valid_subscription,
        auto_request_id=False,
        authentication_policy=authentication_policy,
    ) as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request, **kwargs):
        return base_send_request(client, request, **kwargs)
    return _send_request


def test_client_request_id_in_exception(send_request):
    request = xms_client_request_id.build_get_request()
    with pytest.raises(HttpResponseError):
        send_request(request)

def test_xms_request_client_id_in_client_none(send_request):
    request = xms_client_request_id.build_get_request()
    send_request(request, request_id=None)

def test_xms_request_client_id_in_client(send_request):
    request = xms_client_request_id.build_get_request()
    send_request(request, request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

def test_xms_request_client_overwrite_via_parameter(client_no_request_id):
    # We DON'T support a Swagger parameter for request_id, the request_id policy will overwrite it.
    # We disable the request_id policy for this test
    request = xms_client_request_id.build_param_get_request(x_ms_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")
    response = client_no_request_id.send_request(request)
    response.raise_for_status()

def test_xms_custom_named_request_id(send_request):
    request = header.build_custom_named_request_id_request(foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")
    send_request(request)

def test_xms_custom_named_request_id_parameter_group(send_request):
    request = header.build_custom_named_request_id_param_grouping_request(foo_client_request_id="9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")
    send_request(request)
