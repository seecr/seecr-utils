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

from unittest import TestCase
from seecr.utils import string

class StringsTest(TestCase):

    def setUp(self):
        self.s = string("aap/noot/mies/boom")

    def testCompare(self):
        self.assertEquals("aap/noot/mies/boom", self.s)
    
    def testAfter(self):
        self.assertEquals("noot/mies/boom", self.s.after('aap/'))
        self.assertEquals("", self.s.after('boom'))
        self.assertEquals("aap/noot/mies/boom", self.s.after(''))
        self.assertEquals("", self.s.after('vuur'))
    
    def testBefore(self):
        self.assertEquals("aap/noot", self.s.before('/mies'))
        self.assertEquals("", self.s.before('aap'))
        self.assertEquals("aap/noot/mies/boom", self.s.before(''))
        self.assertEquals("aap/noot/mies/boom", self.s.before('vis'))

    def testPatterns(self):
        self.assertEquals("noot/mies", self.s.after('/').before('/'))
        self.assertEquals("vuur", string("boom vuur vis").after(' ').before(' '))
        self.assertEquals("vis", string("boom vis").after(' ').before(' '))
        self.assertEquals("tom vera", string("bob tom vera carl").after('bob ').before(' carl'))

    def testSyntaxSugar(self):
        self.assertEquals('a', self.s[1])
        self.assertEquals("aap/noot/mies", self.s[:'/'])
        self.assertEquals("noot/mies/boom", self.s['/':])
        self.assertEquals("noot/mies", self.s['/':'/'])
        self.assertEquals('p', self.s[2])
        self.assertEquals('oo', self.s[5:7])
        self.assertEquals(3, self.s['/'])
        self.assertRaises(ValueError, lambda: self.s['x'])

