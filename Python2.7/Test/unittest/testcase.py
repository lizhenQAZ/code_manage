#!yusr/bin/python
# -*- coding:utf-8 -*-
import unittest

class testCase1(unittest.TestCase):
    def setUp(self):
        print "test begin>>>"
    def tearDown(self):
        print "test end<<<"
    def test_fun1(self):
        print "chifan"
    def test_fun2(self):
        print "heshui"

def testSuite():
    suite = unittest.TestSuite()
    suite.addTest(testCase1("test_fun1"))
    suite.addTest(testCase1("test_fun2"))
    unittest.TextTestRunner().run(suite)