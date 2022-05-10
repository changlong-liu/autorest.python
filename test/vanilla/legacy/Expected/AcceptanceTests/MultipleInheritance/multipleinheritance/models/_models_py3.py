# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

import msrest.serialization


class Feline(msrest.serialization.Model):
    """Feline.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    """

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
    }

    def __init__(self, *, meows: Optional[bool] = None, hisses: Optional[bool] = None, **kwargs):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        """
        super().__init__(**kwargs)
        self.meows = meows
        self.hisses = hisses


class Pet(msrest.serialization.Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, name: str, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.name = name


class Cat(Pet, Feline):
    """Cat.

    All required parameters must be populated in order to send to Azure.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    :ivar name: Required.
    :vartype name: str
    :ivar likes_milk:
    :vartype likes_milk: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
        "name": {"key": "name", "type": "str"},
        "likes_milk": {"key": "likesMilk", "type": "bool"},
    }

    def __init__(
        self,
        *,
        name: str,
        meows: Optional[bool] = None,
        hisses: Optional[bool] = None,
        likes_milk: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        :keyword name: Required.
        :paramtype name: str
        :keyword likes_milk:
        :paramtype likes_milk: bool
        """
        super().__init__(name=name, meows=meows, hisses=hisses, **kwargs)
        self.meows = meows
        self.hisses = hisses
        self.likes_milk = likes_milk
        self.name = name


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


class Horse(Pet):
    """Horse.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar is_a_show_horse:
    :vartype is_a_show_horse: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_a_show_horse": {"key": "isAShowHorse", "type": "bool"},
    }

    def __init__(self, *, name: str, is_a_show_horse: Optional[bool] = None, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword is_a_show_horse:
        :paramtype is_a_show_horse: bool
        """
        super().__init__(name=name, **kwargs)
        self.is_a_show_horse = is_a_show_horse


class Kitten(Cat):
    """Kitten.

    All required parameters must be populated in order to send to Azure.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    :ivar name: Required.
    :vartype name: str
    :ivar likes_milk:
    :vartype likes_milk: bool
    :ivar eats_mice_yet:
    :vartype eats_mice_yet: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
        "name": {"key": "name", "type": "str"},
        "likes_milk": {"key": "likesMilk", "type": "bool"},
        "eats_mice_yet": {"key": "eatsMiceYet", "type": "bool"},
    }

    def __init__(
        self,
        *,
        name: str,
        meows: Optional[bool] = None,
        hisses: Optional[bool] = None,
        likes_milk: Optional[bool] = None,
        eats_mice_yet: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        :keyword name: Required.
        :paramtype name: str
        :keyword likes_milk:
        :paramtype likes_milk: bool
        :keyword eats_mice_yet:
        :paramtype eats_mice_yet: bool
        """
        super().__init__(meows=meows, hisses=hisses, name=name, likes_milk=likes_milk, **kwargs)
        self.eats_mice_yet = eats_mice_yet
