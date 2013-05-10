## begin license ##
#
# All rights reserved.
#
# Copyright (C) 2013 Seecr (Seek You Too B.V.) http://seecr.nl
#
## end license ##

from os.path import isdir, makedirs

def ensureDirectoryExists(directory):
    isdir(directory) or makedirs(directory)
    return directory
