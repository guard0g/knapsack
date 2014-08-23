#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def belgian_chocolate(items,capacity):
    itemcount = len(items)
    density = items
    for i in range(itemcount):
        density[i][0] = density[i][2]/density[i][1]
    dens = sorted(density)
    estimate = 0
    count = 0
    c = capacity
    while c > 0:
        estimate += dens[count][2]
        c -= dens[count][1]
        count += 1
    return estimate


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    print
    items.sort()
    print
    


    #Optimization algo here
"""
    value = 0
    weight = 0
    taken = [0]*item_count

    keep = [[0 for j in range(capacity+1)] for i in range(item_count)]
    vsub = [[0 for j in range(capacity+1)] for i in range(item_count)]
    
    for i in range(item_count):
        for j in range(capacity+1):
            value = items[i].value
            weight = items[i].weight
            if (weight <= j) and (value + vsub[i-1][j-weight] > vsub[i-1][j]):
                vsub[i][j]=value + vsub[i-1][j-weight]
                keep[i][j] = 1
            else:
                vsub[i][j] = vsub[i-1][j]
                keep[i][j]=0
    value = vsub[i][j]

    k = capacity    
    for i in range(item_count-1,0,-1):
        if keep[i][k] == 1:
            taken[i] = 1
            k -= items[i].weight        
      
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        #file_location = sys.argv[1].strip()
        file_location="./data/ks_400_0"
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

