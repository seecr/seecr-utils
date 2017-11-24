## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2017 Seecr (Seek You Too B.V.) http://seecr.nl
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
import re

class string(unicode):

    def after(self, substring):
        try:
            return string(self[self.index(substring)+len(substring):])
        except ValueError:
            return string()

    def before(self, substring):
        try:
            return string(self[:self.rindex(substring)])
        except ValueError:
            return self

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.after(i.start or '').before(i.stop or '')
        if isinstance(i, basestring):
            return self.index(i)
        return unicode.__getitem__(self, i)

    def kebab(self):
        return self.rejoin('-', unicode.lower)

    def camel(self):
        return self.rejoin('', unicode.capitalize)

    def rejoin(self, sep, f):
        return string(sep.join(f(fragment) for fragment in self.split()))

    def split(self):
        return (fragment for fragment in split.split(self) if fragment not in ('', '-', '_'))

split = re.compile('([A-Z]{2,}|[A-Z]?[a-z0-9]+)[\-_]?')
