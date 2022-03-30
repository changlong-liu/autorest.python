# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import Any, AsyncIterable, TYPE_CHECKING, Union, cast
from azure.core.polling import AsyncLROPoller

from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated, JSONObject
from ...models import *  # pylint: disable=wildcard-import,unused-wildcard-import


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    async def get_model(self, mode: str, **kwargs: Any) -> Product:
        response = await super().get_model(mode, **kwargs)
        return Product(**response)

    async def post_model(self, mode: str, input: Union[Product, JSONObject], **kwargs: Any) -> Product:
        response = await super().post_model(mode, input, **kwargs)
        return Product(**response)

    def get_pages(self, mode: str, **kwargs) -> AsyncIterable[Product]:
        pages = super().get_pages(mode, cls=lambda objs: [Product(**x) for x in objs], **kwargs)
        return cast(AsyncIterable[Product], pages) # be safe since calling get_pages with Product

    async def begin_lro(self, mode: str, **kwargs: Any) -> AsyncLROPoller[LROProduct]: # type: ignore
        lro = await super().begin_lro(
            mode,
            cls=lambda pipeline_response, deserialized, headers: LROProduct._from_dict(  # pylint: disable=protected-access
                **deserialized
            ),
            **kwargs
        )
        return cast(AsyncLROPoller[LROProduct], lro) # be safe since calling begin_lro with LROProduct


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't otherwise do with the following handwritten customizations framework
    aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = [
    "DPGClientOperationsMixin"
]  # only add objects you want to be publicly available to your users at your package level
