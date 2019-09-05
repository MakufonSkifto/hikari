#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""
A role within a guild.
"""
from __future__ import annotations

import dataclasses

from hikari.core.model import base
from hikari.core.model import color as _color
from hikari.core.model import permission as _permission


@dataclasses.dataclass()
class Role(base.Snowflake):
    """
    Representation of a role within a guild.
    """

    __slots__ = ("id", "name", "color", "hoist", "position", "permissions", "managed", "mentionable")

    #: The ID of the role.
    #:
    #: :type: :class:`int`
    id: int

    #: The name of the role.
    #:
    #: :type: :class:`str`
    name: str

    #: The color of the role.
    #:
    #: :type: :class:`hikari.core.model.color.Color`
    color: _color.Color

    #: Whether the role will be hoisted (show as a separate list in the member list)
    #:
    #: :type: :class:`bool`
    hoist: bool

    #: The position of the role.
    #:
    #: :type: :class:`int`
    position: int

    #: The permissions for the role.
    #:
    #: :type: :class:`hikari.core.model.permission.Permission`
    permissions: _permission.Permission

    #: True if the role is created by an integration or by adding a bot to the server, or False otherwise.
    #:
    #: :type: :class:`bool`
    managed: bool

    #: True if you can mention this role and thus ping all members in that role at once, False if you can not.
    #:
    #: :type: :class:`bool`
    mentionable: bool

    def __init__(self, payload):
        self.id = int(payload["id"])
        self.name = payload["name"]
        self.color = _color.Color(payload["color"])
        self.hoist = payload["hoist"]
        self.position = payload["position"]
        self.permissions = _permission.Permission(payload["permissions"])
        self.managed = transform.get_cast(payload, "managed", bool)
        self.mentionable = transform.get_cast(payload, "mentionable", bool)


__all__ = ["Role"]
