#!yusr/bin/python
# -*- coding:utf-8 -*-
import unittest
import testcase

if __name__=='__main__':
    log_file="log_file.txt"
    f=open(log_file,"w")
    runner=unittest.TextTestRunner(stream=f,verbosity=2)
    unittest.main(exit=f,testRunner=runner)
    f.close()