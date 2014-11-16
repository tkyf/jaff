# -*- coding: utf-8 -*-

import unittest

import mecab_wrapper

class MeCabWrpperTest(unittest.TestCase):
    
    def setUp(self):
        self.inputs = ['こんにちは']

    def test_tagging(self):
        for string in self.inputs:
            mecab_wrapper.tagging(string)


if __name__ == '__main__':
    unittest.main()
