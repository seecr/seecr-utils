# -*- coding: utf-8 -*-
## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2005-2009 Seek You Too (CQ2) http://www.cq2.nl
# Copyright (C) 2012-2014 Seecr (Seek You Too B.V.) http://seecr.nl
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

from sys import path                            #DO_NOT_DISTRIBUTE
from os import system, listdir                  #DO_NOT_DISTRIBUTE
from os.path import isdir, join                 #DO_NOT_DISTRIBUTE
system("find .. -name '*.pyc' | xargs rm -f")   #DO_NOT_DISTRIBUTE
if isdir('../deps.d'):                          #DO_NOT_DISTRIBUTE
    for d in listdir('../deps.d'):              #DO_NOT_DISTRIBUTE
        path.insert(0, join('../deps.d', d))    #DO_NOT_DISTRIBUTE
path.insert(0, '..')                            #DO_NOT_DISTRIBUTE

import unittest

from directorytest import DirectoryTest
from debugprompttest import DebugPromptTest
from versiontest import VersionTest

if __name__ == '__main__':
    unittest.main()

