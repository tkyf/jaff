#!/usr/bin/env python
#coding:utf-8

import unittest

import compare

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            (u"こんにちはわたしは元気です", u"こにちわわちしは元気でした")
            ]
        self.expect = [
            (u"こんにちは\tわたし\tは\t元気\tです",
                u"こにちわ\tわちし\tは\t元気\tでした",
                u"感動詞\t名詞\t助詞\t名詞\t助動詞")
            ]

    def test_compare(self):
        self.assertEqual(compare.compare(input[0][0], input[0][1]), self.expect[0])

if __name__ == "__main__":
    unittest.main()
