#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    key_part, value_part = line.split('\t')
    
    key_list = key_part.split(':')
    node_id = int(key_list[1])
    if len(key_list) > 2:
        iter_no = int(key_list[2])
    else:
        iter_no = 1

    value_list = value_part.split(',')
    curr_rank = float(value_list[0])
    prev_rank = float(value_list[1])
    neighbors = value_list[2:]
    d = len(neighbors)
    
    outline = '#\t%d,%f,%d\n' % (node_id, curr_rank, iter_no)    
    sys.stdout.write(outline)
    if d > 0:
        i = node_id
        r_dist = curr_rank / float(d)
        for j in neighbors:
            outline = '%d\t%d,%f\n' % (int(j), i, r_dist)
            sys.stdout.write(outline)
    else:
        i = node_id
        outline = '%d\t%d,%f\n' % (i, i, curr_rank)
        sys.stdout.write(outline)

    
        
