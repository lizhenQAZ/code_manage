#!usr/bin/python
# -*- coding:utf-8 -*-

import sys

print dir(sys)
print "*********************************"
print help(sys)
print "*********************************"
print help(sys.__doc__)
print "*********************************"

#sys.argv
print sys.argv[0]
print "*********************************"

#sys.exit
"""
def exitfunc(value):
    print value
    sys.exit(0)
print "hello world!"
try:
    sys.exit(1)
except SystemExit,exception:
    exitfunc(exception)
print "the end!"
print "*********************************"
"""

#sys.path
print sys.path
sys.path.append("C:/")
print sys.path
sys.path.remove("C:/")
print sys.path
print "*********************************"

#sys,modules
print sys.modules.keys()
print sys.modules.values()
print sys.modules["os"]
print "*********************************"

#sys.stdin stdout stderr
print sys.stdin
print "*********************************"
dir(sys.stdin)
print "*********************************"
help(sys.stdin)
print "*********************************"
print(sys.stdin.__doc__)
print "*********************************"

#sys.platform
print sys.platform

#sys.getdefaultencoding() sys.setdefaultencoding sys.getfilesystemencoding
print sys.getdefaultencoding()
#sys.setdefaultencoding('utf8') not exist
print sys.getfilesystemencoding()