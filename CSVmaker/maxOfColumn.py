#!/usr/bin/python
# FUNCTION: Returns the maximum value in column $2 of file $1. Must be a CSV.

import csv
import sys

# Saves the column of a csv to a dictionary
def csv_col_to_dict(filename, column):
    dict = {}
    reader = csv.DictReader(open(filename, 'r'))        

    for line in reader:
        key = line.values()[0]
        value = int(line.values()[int(column)-1])
        dict[key] = value

    return dict


def main():
    dictionary = csv_col_to_dict(sys.argv[1], sys.argv[2])
    max_value = max(dictionary.values())    
    print "Max value: " + str(max_value)

if __name__ == "__main__":
    main()       
