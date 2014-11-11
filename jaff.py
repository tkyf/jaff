#!/usr/bin/env python
# coding:utf-8

def jaff(str1, str2):
    import mecab_wrapper
    import alignment.align

    a = alignment.align.align(str1, str2)
    m = mecab_wrapper.tagging(str1)
    print(a)
    print(m)
    return ""


def main():
    import sys

    import mecab_wrapper
    import alignment.align

    if len(sys.argv) != 3:
        print("Usage: $ python jaff.py textfile1 textfile2")
        return 1

    base = sys.argv[1]
    target = sys.argv[2]

    a = alignment.align.align(base, target)
    print(a)

    mb = mecab_wrapper.tagging(base)
    print(mb)
    mt = mecab_wrapper.tagging(target)
    print(mt)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
