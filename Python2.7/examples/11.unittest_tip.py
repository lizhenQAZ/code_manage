#!yusr/bin/python
# -*- coding:utf-8 -*-
import unittest


class TestCase1(unittest.TestCase):
    def setUp(self):
        print "test begin>>>"

    def tearDown(self):
        print "test end<<<"

    def test_fun1(self):
        print "chifan"

    def test_fun2(self):
        print "heshui"


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCase1("test_fun1"))
    suite.addTest(TestCase1("test_fun2"))
    return suite


if __name__ == '__main__':
    unittest_file = "11_unittest.txt"
    f = open(unittest_file, "w")
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    unittest.main(exit=f, testRunner=runner)
    f.close()
