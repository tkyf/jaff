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
            ('こんにちは\tわたし\tは\t元気\tです',
                'こにちわ\tわちし\tは\t元気\tでした',
                '感動詞\t名詞-代名詞-一般\t助詞-係助詞\t名詞-形容動詞語幹\t助動詞'),
            ("こんにちは", "こんにちは", "感動詞")
            ]

    def test_compare(self):
        for (i, e) in zip (self.input, self.expect):
            self.assertEqual(jaff.jaff(i[0], i[1]), e)


if __name__ == "__main__":
    unittest.main()
