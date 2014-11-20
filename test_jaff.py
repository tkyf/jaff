#!/usr/bin/env python
# coding:utf-8

import unittest

import jaff


class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            ("こんにちはわたしは元気です", "こにちわわちしは元気でした"),
            ("こんにちは", "こんにちは")
            ]
        self.expect = [
            ("こんにちは\tわたし\tは\t元気\tです",
                "こにちわ\tわちし\tは\t元気\tでした",
                "感動詞\t名詞\t助詞\t名詞\t助動詞"),
            ("こんにちは", "こんにちは", "感動詞")
            ]

    def test_compare(self):
        for (i, e) in zip (self.input, self.expect):
            self.assertEqual(jaff.jaff(i[0][0], i[0][1]), e)


if __name__ == "__main__":
    unittest.main()