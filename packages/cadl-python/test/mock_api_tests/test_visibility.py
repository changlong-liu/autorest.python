# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from models.visibility import models, VisibilityClient


@pytest.fixture
def client():
    with VisibilityClient() as client:
        yield client


def test_get(client: VisibilityClient):
    assert client.get_model(models.VisibilityModel(required_query_int32=123)
                            ) == {
        "requiredReadonlyString": "abc",
    }


def test_head(client: VisibilityClient):
    assert client.head_model(models.VisibilityModel(
        required_query_int32=123)) == True


def test_put(client: VisibilityClient):
    client.put_model(models.VisibilityModel(
        required_create_string_list=["foo", "bar"], required_update_int_list=[1, 2]))


def test_post(client: VisibilityClient):
    client.post_model(models.VisibilityModel(
        required_create_string_list=["foo", "bar"]))


def test_patch(client: VisibilityClient):
    client.patch_model(models.VisibilityModel(
        required_update_int_list=[1, 2]))


def test_delete(client: VisibilityClient):
    client.delete_model(models.VisibilityModel(
        required_delete_boolean=True))
