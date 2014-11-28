#!/usr/bin/env python
# coding:utf-8

import unittest
import align


class TestAlign(unittest.TestCase):

    def setUp(self):
        blank = '\t'

        self.cases = [(("A", "A"), ("A", "A")),
                      (("A", "B"), ("A", "B")),
                      (("AB", "A"), ("AB", "A" + blank)),
                      (("BA", "A"), ("BA", blank + "A")),
                      (("ABA", "AA"), ("ABA", "A" + blank + "A")),
                      (("BAB", "A"), ("BAB", blank + "A" + blank)),
                      (("A", ""), ("A", "")),
                      (("", "A"), ("", "A")),
                      (("", ""), ("", ""))
                      ]

        self.jcases = [(("あ", ""), ("あ", "")),
                       (("", "あ"), ("", "あ")),
                       (("あ", "あ"), ("あ", "あ")),
                       (("あいあ", "ああ"), ("あいあ", "あ" + blank + "あ")),
                       (("ああ", "あいあ"), ("あ" + blank + "あ", "あいあ")),
                       (("あ", "あいあ"), ("あ" + blank + blank, "あいあ")),
                       (("です", "ですた"), ("です" + blank, "ですた")),
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
