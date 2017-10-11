#!/usr/bin/python
# FUNCTION: Returns the maximum value in column $2 of file $1. Must be a CSV.

import sys
import os
import re

def main():
    filename = sys.argv[1]
    column = int(sys.argv[2])
    max_value = -1

    with open(filename, 'r') as file:
        next(file)
        current_value = 0
        for line in file:
            current_value = int(line.split(',')[column-1])
            if current_value > max_value:
                max_value = current_value

    print "Max value: ", str(max_value)

if __name__ == "__main__":
    main()
