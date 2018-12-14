## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2018 Seecr (Seek You Too B.V.) https://seecr.nl
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

from seecr.test import SeecrTestCase

from seecr.tools import atomic_write
from os.path import isfile, join

class AtomicWriteTest(SeecrTestCase):
    def testAtomicWrite(self):
        filename = join(self.tempdir, "testfile")
        self.assertFalse(isfile(filename))
        with atomic_write(filename) as fp:
            self.assertFalse(isfile(filename))
            self.assertTrue(isfile("{}.tmp".format(filename)))
            fp.write("This is the test")
            self.assertFalse(isfile(filename))

        self.assertFalse(isfile("{}.tmp".format(filename)))
        self.assertTrue(isfile(filename))
        self.assertEqual("This is the test", open(filename).read())
