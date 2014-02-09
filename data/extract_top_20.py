#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
rank_list = []
for line in sys.stdin:
    key_part, value_part = line.strip().split('\t')
    
    key_list = key_part.split(':')
    node = key_list[1]

    value_list = value_part.split(',')
    rank = float(value_list[0])
    
    rank_list.append([-rank, node])

rank_list.sort()
for i in range(40):
    if i == 20:
        sys.stdout.write('\n');
    outline = 'FinalRank:%f\t%s\n' % (-rank_list[i][0], rank_list[i][1])
    sys.stdout.write(outline)
    
        
