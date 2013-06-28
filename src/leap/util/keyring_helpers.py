# -*- coding: utf-8 -*-
# privilege_policies.py
# Copyright (C) 2013 LEAP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

"""

import keyring

OBSOLETE_KEYRINGS = [
    keyring.backends.file.EncryptedKeyring,
    keyring.backends.file.PlaintextKeyring
]


def has_keyring():
    """

    """
    kr = keyring.get_keyring()
    return kr is not None and kr.__class__ not in OBSOLETE_KEYRINGS
