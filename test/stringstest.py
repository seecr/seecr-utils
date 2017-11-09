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

