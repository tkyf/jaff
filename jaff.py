#!/usr/bin/env python
# coding:utf-8

def main():
    import argparse
    import sys

    import align.align

    #TODO argparseで引数を処理
    parser = argparse.ArgumentParser(description="Get word diff with POS.")
    parser.add_argument("-s", "--stats", dest="s", action="store_true", help="Calculate word diff statistics")
    parser.add_argument("-a", "--all", dest="a", action="store_true", help="    Output all texts")
    args = parser.parse_args()

    if len(sys.argv) != 3:
        print("Usage: $ python jaff textfile1 textfile2")
        return 1
    
    base = sys.argv[1]
    base = sys.argv[2]

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())

