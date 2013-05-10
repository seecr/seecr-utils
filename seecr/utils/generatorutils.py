## begin license ##
#
# All rights reserved.
#
# Copyright (C) 2013 Seecr (Seek You Too B.V.) http://seecr.nl
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
            g.next()
    except StopIteration, e:
        return e.args[0] if e.args else None