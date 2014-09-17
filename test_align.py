#!/usr/bin/env python
#coding:utf-8

import unittest

from alignment.align import align

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            ("こんにちはわたしは元気です", "こにちわわちしは元気でした")
            ]
        self.expect = [
            ("こんにちは\tわたし\tは\t元気\tです",
                "こにちわ\tわちし\tは\t元気\tでした",
                "感動詞\t名詞\t助詞\t名詞\t助動詞")
            ]

    def test_compare(self):
        self.assertEqual(align(self.input[0][0], self.input[0][1]), self.expect[0])

if __name__ == "__main__":
    unittest.main()

