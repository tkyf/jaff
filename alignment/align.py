#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
import sys


def align(str1, str2):
    """Calculate global alignment of two strings with Needleman-Wunsch algorithm.

    param: str1: one of strings.
    param: str2: the other one of strings.
    """
    if str1 == "" or str2 == "":
        return (str1, str2)

    table = Table(str1, str2)
    return table.get_alignment()


class Table(object):
    """Table for calcuration global alignment by dynamic programming.
    """

    blank = "\t"

    class Cell(object):
        """One of cell in tabel.
        """
        def __init__(self, table, row, col):
            self.table = table
            self.row = row
            self.col = col
            self.score = 0
            self.prev_cell = None

        def initialize_score(self):
            if self.row == 0 and self.col != 0:
                self.score = self.table.score_table[self.row][self.col - 1].score - 2
            elif self.row != 0 and self.col == 0:
                self.score = self.table.score_table[self.row - 1][self.col].score - 2
            else:
                self.score = 0

        def initialize_prev_cell(self):
            if self.row == 0 and self.col != 0:
                self.prev_cell = self.table.score_table[self.row][self.col - 1]
            elif self.row != 0 and self.col == 0:
                self.prev_cell = self.table.score_table[self.row - 1][self.col]
            else:
                self.prev_cell = None

        def __str__(self):
            return str(self.score)

        def fill_in_cell(self, above_cell, left_cell, aboveleft_cell):
            from_left_score = left_cell.score - 2
            from_above_score = above_cell.score - 2

            if (self.table.str1[self.col - 1] == self.table.str2[self.row - 1]):
                from_aboveleft_score = aboveleft_cell.score + 1
            else:
                from_aboveleft_score = aboveleft_cell.score - 1

            self.score = max(from_left_score, from_above_score, from_aboveleft_score)
            if (self.score == from_left_score):
                self.prev_cell = left_cell
            elif (self.score == from_above_score):
                self.prev_cell = above_cell
            else:
                self.prev_cell = aboveleft_cell

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.score_table = []
        self._initialize()

    def __str__(self):
        return str([[str(cell) for cell in row] for row in self.score_table])

    def _initialize(self):
        self.score_table = [[Table.Cell(self, i, j) for j in range(len(self.str1) + 1)] for i in range(len(self.str2) + 1)]
        for row in self.score_table:
            for cell in row:
                cell.initialize_score()
                cell.initialize_prev_cell()

    # Calcurate Global alignment
    def calcurate(self):
        if not hasattr(self, 'alignment'):
            self._fill_in()
            self.alignment = self._get_trace_back()

    def get_alignment(self):
        self.calcurate()
        return self.alignment

    def _fill_in(self):
        for i, row in enumerate(self.score_table):
            if i == 0:
                continue
            for j, cell in enumerate(row):
                if j == 0:
                    continue
                above_cell = self.score_table[i - 1][j]
                left_cell = self.score_table[i][j - 1]
                aboveleft_cell = self.score_table[i - 1][j - 1]
                cell.fill_in_cell(above_cell, left_cell, aboveleft_cell)

    def _get_trace_back(self):
        aligned_str1 = ""
        aligned_str2 = ""
        current_cell = self.score_table[len(self.str2)][len(self.str1)]

        while(current_cell.prev_cell != None):
            prev_cell = current_cell.prev_cell
            if (current_cell.row - prev_cell.row) == 1:
                aligned_str2 = self.str2[current_cell.row - 1] + aligned_str2
            else:
                aligned_str2 = self.blank + aligned_str2

            if (current_cell.col - prev_cell.col) == 1:
                aligned_str1 = self.str1[current_cell.col - 1] + aligned_str1
            else:
                aligned_str1 = self.blank + aligned_str1

            current_cell = current_cell.prev_cell

        return aligned_str1, aligned_str2

    def print_table(self):
        self.calcurate()
        print("          " + "    ".join(self.str1))
        print("   " + str([str(cell) for cell in self.score_table[0]]))
        for i, c in enumerate(" " + self.str2):
            if i == 0:
                continue
            print(" {0} {1}".format(c, [str(cell) for cell in self.score_table[i]]))


def main():
    if len(sys.argv) != 3:
        print('Usage: $ python align.py string1 string2')
        return 1

    alignment = align(sys.argv[1], sys.argv[2])
    print(alignment)

    return 0


if __name__ == '__main__':
    sys.exit(main())
