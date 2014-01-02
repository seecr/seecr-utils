## begin license ##
#
# "Seecr Utils" is a package with a wide range of valuable tools.
#
# Copyright (C) 2013 Seecr (Seek You Too B.V.) http://seecr.nl
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

from weightless.core import compose

def generatorReturn(value):
    raise StopIteration(value)

def asGenerator(f):
    def g(*args, **kwargs):
        raise StopIteration(f(*args, **kwargs))
        yield
    return g

def returnValueFromGenerator(g):
    g = compose(g)
    try:
        while True:
            next(g)
    except StopIteration as e:
        return e.args[0] if e.args else None

def asList(g):
    return list(compose(g))

def asString(g):
    return ''.join(compose(g))

def consume(g):
    for _ in compose(g): pass
