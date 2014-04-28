## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2014 Seecr (Seek You Too B.V.) http://seecr.nl
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


class Version(object):
    def __init__(self, versionString):
        self._versionString = versionString

    def __cmp__(self, other):
        return cmp(self.asTuple(), other.asTuple())

    def __hash__(self):
        return hash(self.__class__) ^ hash(self._versionString)

    def asTuple(self):
        return tuple(asint(p) for p in self._versionString.split('.'))

    def majorVersion(self):
        return '{0}.{1}'.format(*self.asTuple())

    def nextMajorVersion(self):
        first, second = self.asTuple()[:2]
        return '{0}.{1}'.format(first, second + 1)

    def __str__(self):
        return self._versionString

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, repr(self._versionString))

def asint(aString):
    if aString == 'x':
        return object()
    return int(aString)
