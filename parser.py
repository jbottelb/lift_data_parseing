#!/usr/bin/env python

# there are 7 header rows


import csv, sys

file = sys.argv[1]

with open(file) as csvfile:
    f = list(csv.reader(csvfile))

    i = 0
    Athlete = 0

    seen_names = {}

    for row in f:
        if i < 8:
            pass
        else:
            if row[0] in seen_names:
                row[0] = seen_names[row[0]]
            else:
                seen_names[row[0]] = "Athlete " + str(Athlete)
                Athlete += 1
                row[0] = seen_names[row[0]]
        i += 1

    for row in f:
        print(row)
