# --------------------------------------------------------------------------
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
from mediatypeslowlevel import MediaTypesClient
from mediatypeslowlevel.rest import *
import json
import pytest

@pytest.fixture
def client():
    with MediaTypesClient() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

def test_pdf(send_request_json_response):
    request = build_analyze_body_request(content=b"PDF", content_type="application/pdf")
    assert send_request_json_response(request) == "Nice job with PDF"

def test_json(send_request_json_response):
    request = build_analyze_body_request(json={"source":"foo"})
    assert send_request_json_response(request) == "Nice job with JSON"

def test_content_type_with_encoding(send_request_json_response):
    request = build_content_type_with_encoding_request(content="hello", content_type='text/plain; charset=UTF-8')
    assert send_request_json_response(request) == "Nice job sending content type with encoding"

def test_pdf_no_accept_header(send_request):
    request = build_analyze_body_no_accept_header_request(content=b"PDF", content_type="application/pdf")
    send_request(request)

def test_json_no_accept_header(send_request):
    request = build_analyze_body_no_accept_header_request(json={"source":"foo"})
    send_request(request)

def test_binary_body_two_content_types(send_request):
    json_input = json.dumps({"hello":"world"})
    request = build_binary_body_with_two_content_types_request(content=json_input, content_type="application/json")
    send_request(request)

    content = b"hello, world"
    request = build_binary_body_with_two_content_types_request(content=content, content_type="application/octet-stream")
    send_request(request)

def test_binary_body_three_content_types(send_request):
    json_input = json.dumps({"hello":"world"})
    request = build_binary_body_with_three_content_types_request(content=json_input, content_type="application/json")
    send_request(request)

    content = b"hello, world"
    request = build_binary_body_with_three_content_types_request(content=content, content_type="application/octet-stream")
    send_request(request)

    content = "hello, world"
    request = build_binary_body_with_three_content_types_request(content=content, content_type="text/plain")
    send_request(request)
