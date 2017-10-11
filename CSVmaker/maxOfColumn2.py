#!/usr/bin/python
# FUNCTION: Returns the maximum value in column $2 of file $1. Must be a CSV.

import sys
import os
import re

def main():
    filename = sys.argv[1]
    column = int(sys.argv[2])
    max_value = 0
    reg_expr = ""

    file = open(filename, 'r')

    # Count number of commas in header + check valid column input.
    numCommas = file.readline().count(',')
    if column < 1 or column > numCommas+1:
        print "Invalid column."
        sys.exit(0)

    # Build the regular expression.
    for i in xrange(column-1):
        reg_expr += ".*," 
    reg_expr += "(.*),"
    for i in xrange(column-1, numCommas):
        reg_expr += ".*,"
    reg_expr = reg_expr[:-1]

    print "Regular expression used: ", reg_expr    

    # Check the column value in each row
    current_value = 0
    for line in file:
        current_value = int(re.match(reg_expr, line).group(1))
        if current_value > max_value:
            max_value = current_value

    print "Max value: ", str(max_value)

if __name__ == "__main__":
    main()
