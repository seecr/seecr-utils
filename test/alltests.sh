#!/bin/bash
## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2012-2014 Seecr (Seek You Too B.V.) https://seecr.nl
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

export LANG=en_US.UTF-8
export PYTHONPATH=.:"$PYTHONPATH"
pyversions=""
for v in 2.6 2.7; do
    if [ -e /usr/bin/python${v} ]; then
        pyversions="$pyversions python${v}"
    fi
done

option=$1
if [ "${option:0:10}" == "--python2." ]; then
    shift
    pyversions="${option:2}"
fi
echo Found Python versions: $pyversions
for pycmd in $pyversions; do
    echo "================ $pycmd _alltests.py $@ ================"
    $pycmd _alltests.py "$@"
done

