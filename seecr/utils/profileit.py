## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2005-2009 Seek You Too (CQ2) http://www.cq2.nl
# Copyright (C) 2012-2013 Seecr (Seek You Too B.V.) https://seecr.nl
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

from hotshot import Profile
from os import system

def profile(func, name = 'main', runKCacheGrind = False):
	prof = Profile('/tmp/' + name + '.prof', lineevents=1, linetimings=1)
	try:
		prof.runcall(func)
	finally:
		prof.close()
	# For running KCacheGrind you need to install (aptitude):
	# - kcachegrind
	# - kcachegrind-convertors
	if runKCacheGrind:
		path = '/'.join(__file__.split('/')[:-1])
		system('hotshot2calltree -o /tmp/%(name)s.out /tmp/%(name)s.prof; kcachegrind /tmp/%(name)s.out' % locals())

