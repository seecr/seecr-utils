## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2013-2014, 2017-2018, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Seecr Utils"
#
# "Seecr Utils" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Seecr Utils" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr Utils"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from .directory import ensureDirectoryExists
from .systemutils import isRootUser
from .debugprompt import DebugPrompt
from .atomicwrite import atomic_write
from .readdata import read_from_file
