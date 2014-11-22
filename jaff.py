#!/usr/bin/env python
# coding:utf-8

def jaff(str1, str2):
    import mecab_wrapper
    import alignment.align

    a = alignment.align.align(str1, str2)
    m = mecab_wrapper.tagging(str1)
    print(a)
    pos_alignment = pos_align(a, m)
    return (a[0], a[1], pos_alignment)

def pos_align(alignment, tags, blank="\t"):
    for i, c in enumerate(alignment[0]):
        if c == blank:
            tags.insert(i, None)

    pos_alignment = ''
    for tag in tags:
        if tag is None:
            pos_alignment += blank
        elif  tag['position'] == 'E':
            pos_alignment += tag['pos']

    return pos_alignment

def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: $ python jaff.py textfile1 textfile2")
        return 1

    base = sys.argv[1]
    target = sys.argv[2]

    jaff(base, target)


if __name__ == "__main__":
    main()
