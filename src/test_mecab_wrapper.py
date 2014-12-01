#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

import mecab_wrapper

class MeCabWrpperTest(unittest.TestCase):
    
# for MeCab UniDic Dictionary
    def setUp(self):
        self.inputs = ['こんにちは', 'こんにちは、私は元気です。']
        self.answers= [[{'surface': 'こ', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ん', 'position': 'I', 'pos': '感動詞'}, {'surface': 'に', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ち', 'position': 'I', 'pos': '感動詞'}, {'surface': 'は', 'position': 'E', 'pos': '感動詞'}],
                [{'surface': 'こ', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ん', 'position': 'I', 'pos': '感動詞'},\
                        {'surface': 'に', 'position': 'I', 'pos': '感動詞'}, {'surface': 'ち', 'position': 'I', 'pos': '感動詞'},\
                        {'surface': 'は', 'position': 'E', 'pos': '感動詞'}, {'surface': '、', 'pos': '記号-読点', 'position':'E'},\
                        {'surface': '私', 'pos': '名詞-代名詞-一般', 'position': 'E'}, {'surface': 'は', 'pos': '助詞-係助詞', 'position': 'E'},\
                        {'surface': '元', 'pos': '名詞-形容動詞語幹', 'position': 'I'}, {'surface': '気', 'pos': '名詞-形容動詞語幹', 'position': 'E'},\
                        {'surface': 'で', 'pos': '助動詞', 'position': 'I'}, {'surface':'す', 'pos': '助動詞', 'position': 'E'},\
                        {'surface': '。', 'pos': '記号-句点', 'position': 'E'}]
                ]

    def test_tagging(self):
        for in_str, answer in zip(self.inputs, self.answers):
            self.assertEqual(mecab_wrapper.tagging(in_str), answer)
            print(mecab_wrapper.tagging(in_str))


if __name__ == '__main__':
    unittest.main()
