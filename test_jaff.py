#!/usr/bin/env python
# coding:utf-8

import unittest

import jaff


class Test(unittest.TestCase):
    def setUp(self):
        import MeCab
        try:
# expect using mecab-ipadic
            MeCab.Tagger('-Ochasen')
            self.input = [
                ("こんにちはわたしは元気です", "こにちわわちしは元気でした"),
                ("こんにちは", "こんにちは"),
                ("おはよう", "おはよ")
                ]
            self.expect = [
                ('こんにちは\tわたし\tは\t元気\tです',
                    'こにちわ\tわちし\tは\t元気\tでした',
                    '感動詞\t名詞-代名詞-一般\t助詞-係助詞\t名詞-形容動詞語幹\t助動詞'),
                ("こんにちは", "こんにちは", "感動詞"),
                ("おはよう", "おはよ", "感動詞")
                ]
        except RuntimeError:
# expect using mecab-unidic
            self.input = [
                ("こんにちはわたしは元気です", "こにちわわちしは元気でした"),
                ("こんにちは", "こんにちは"),
                ("おはよう", "おはよ")
                ]
            self.expect = [
                ('こんにちは\tわたし\tは\t元気\tです',
                    'こにちわ\tわちし\tは\t元気\tでした',
                    '感動詞-一般\t代名詞\t助詞-係助詞\t名詞-普通名詞-形状詞可能\t助動詞'),
                ("こんにちは", "こんにちは", "感動詞-一般"),
                ("おはよう", "おはよ", "感動詞-一般")
                ]


    def test_compare(self):
        for (i, e) in zip (self.input, self.expect):
            self.assertEqual(jaff.jaff(i[0], i[1]), e)


if __name__ == "__main__":
    unittest.main()
