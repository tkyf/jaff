#!/usr/bin/env python
# coding:utf-8


def main():
    import sys

    from alignment.align import align

    if len(sys.argv) != 3:
        print("Usage: $ python jaff.py textfile1 textfile2")
        return 1

    base = sys.argv[1]
    target = sys.argv[2]

    alignment = align(base, target)
    print(alignment)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
