## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2014-2015 Seecr (Seek You Too B.V.) http://seecr.nl
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

from seecr.utils import Version

class VersionTest(SeecrTestCase):

    def testVersionX(self):
        self.assertTrue(Version('1.4') <= Version('1.4.x') < Version('1.5'))
        self.assertTrue(Version('1.4.3') <= Version('1.4.x') < Version('1.5'))
        self.assertRaises(Exception, lambda: Version('1.4.development'))

    def testVersionComparisons(self):
        self.assertTrue(Version('1.4') <= Version('1.4.3') < Version('1.5'))
        self.assertFalse(Version('1.4') <= Version('1.3') < Version('1.5'))
        self.assertFalse(Version('1.4') <= Version('1.42.3') < Version('1.5'))
        self.assertTrue(Version('1.4.2') <= Version('1.4.3') < Version('1.5'))
        self.assertFalse(Version('1.4.2') <= Version('1.4') < Version('1.5'))

    def testMajorVersion(self):
        self.assertEquals(Version('1.4'), Version('1.4').majorVersion())
        self.assertEquals(Version('1.4'), Version('1.4.x').majorVersion())
        self.assertEquals(Version('1.4'), Version('1.4.3.2').majorVersion())
        self.assertRaises(Exception, lambda: Version('1').majorVersion())

    def testNextMajorVersion(self):
        self.assertEquals(Version('1.5'), Version('1.4').nextMajorVersion())
        self.assertEquals(Version('1.5'), Version('1.4.x').nextMajorVersion())
        self.assertEquals(Version('1.5'), Version('1.4.3.2').nextMajorVersion())
        self.assertEquals(Version('1.55'), Version('1.54.3.2').nextMajorVersion())
        self.assertRaises(Exception, lambda: Version('1').nextMajorVersion())

    def testVersionAsString(self):
        self.assertEquals('1.4', '%s' % Version('1.4'))
        self.assertEquals('1.4', str(Version('1.4')))
        self.assertEquals('1.4', '{0}'.format(Version('1.4')))

    def testRepr(self):
        self.assertEquals("Version('1.4')", repr(Version('1.4')))

    def testHash(self):
        self.assertEquals(hash(Version('1.5')), hash(Version('1.5')))
        self.assertEquals('value', {Version('1.5'):'value'}[Version('1.5')])

    def testVersionVersion(self):
        self.assertEquals('1.4', '%s' % Version(Version('1.4')))