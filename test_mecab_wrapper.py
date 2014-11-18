#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

import mecab_wrapper

class MeCabWrpperTest(unittest.TestCase):
    
    def setUp(self):
        self.inputs = ['こんにちは']
        self.answers= [[{'surface': 'こ', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ん', 'position': 'I', 'pos': '感動詞'}, {'surface': 'に', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ち', 'position': 'I', 'pos': '感動詞'}, {'surface': 'は', 'position': 'E', 'pos': '感動詞'}]
                ]

    def test_tagging(self):
        for in_str, answer in zip(self.inputs, self.answers):
            self.assertEqual(mecab_wrapper.tagging(in_str), answer)
            print(mecab_wrapper.tagging(in_str))


if __name__ == '__main__':
    unittest.main()
