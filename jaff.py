#!/usr/bin/env python
# coding:utf-8

def main():

    pass

if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser(description="Get word diff with POS.")
    parser.add_option("-s", "--stats", dest="s", action="store_true", help="Calculate word diff statistics")
    parser.add_option("-a", "--all", dest="a", action="store_true", help="    Output all texts")

    (opts, args) = parser.parse_args()

    main()

