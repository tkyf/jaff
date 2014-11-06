#!/usr/bin/env python
# coding:utf-8


def main():
    import sys

    import alignment.align

    if len(sys.argv) != 3:
        print("Usage: $ python jaff.py textfile1 textfile2")
        return 1

    base = sys.argv[1]
    target = sys.argv[2]

    a = alignment.align.align(base, target)
    print(a)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
