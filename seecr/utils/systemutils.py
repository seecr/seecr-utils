## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2005-2009 Seek You Too (CQ2) http://www.cq2.nl
# Copyright (C) 2012-2013 Seecr (Seek You Too B.V.) http://seecr.nl
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

from os import geteuid, setegid, seteuid
from pwd import getpwnam
from grp import getgrnam

def runAs(username, groupname):
    pw_name, pw_passwd, userId, pw_gid, pw_gecos, pw_dir, pw_shell = getpwnam(username)
    gr_name, gr_x, groupId, userlist = getgrnam(groupname)
    assert pw_gid == groupId or pw_name in userlist
    setegid(groupId)
    seteuid(userId)

def isRootUser():
    return geteuid() == 0
