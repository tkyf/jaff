#!/usr/bin/env python
# coding:utf-8

import unittest
import align


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.cases = [(("A", "A"), ("A", "A")),
                      (("A", "B"), ("A", "B")),
                      (("AB", "A"), ("AB", "A-")),
                      (("BA", "A"), ("BA", "-A")),
                      (("ABA", "AA"), ("ABA", "A-A")),
                      (("BAB", "A"), ("BAB", "-A-")),
                      (("A", ""), ("A", "")),
                      (("", "A"), ("", "A")),
                      (("", ""), ("", ""))
                      ]

        self.jcases = [(("あ", ""), ("あ", "")),
                       (("", "あ"), ("", "あ")),
                       (("あ", "あ"), ("あ", "あ")),
                       (("あいあ", "ああ"), ("あいあ", "あ-あ")),
                       (("ああ", "あいあ"), ("あ-あ", "あいあ")),
                       (("あ", "あいあ"), ("あ--", "あいあ")),
                       (("あ", ""), ("あ", "")),
                       (("", "あ"), ("", "あ")),
                       (("", ""), ("", ""))
                       ]

    def test_align(self):
        for case in self.cases:
            self.assertEqual(align.align(case[0][0], case[0][1]), case[1])

    def test_align_with_japanese(self):
        for case in self.jcases:
            self.assertEqual(align.align(case[0][0], case[0][1]), case[1])


if __name__ == '__main__':
    unittest.main()
