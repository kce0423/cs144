#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

alpha = 0.85
iter_no = 0
n = 0 # number of nodes
rank = {} 
rank_sum = 0

for line in sys.stdin:
    key_part, value_part = line.split('\t')
    value_list = value_part.split(',')
        
    if key_part == '#':
        node_i = int(value_list[0])
        r = float(value_list[1])
        iter_no = int(value_list[2])
        if rank.get(node_i) is None:
            rank[node_i] = {'old' : 0, 'new' : 0}
        rank[node_i]['old'] = r
        rank_sum += r
        n += 1
    else:
        node_i = int(key_part)
        n_r = float(value_list[0])
        if rank.get(node_i) is None:
            rank[node_i] = {'old' : 0, 'new' : 0}
        rank[node_i]['new'] = n_r
        neighbors = value_list[1:]
        for node_j in neighbors:
            outline = '%d\t%d\n' % (int(node_j), node_i)
            sys.stdout.write(outline)

residual = (1 - alpha) / float(n) * rank_sum
for key, value in rank.iteritems():
    new_rank = value['new'] * alpha + residual
    old_rank = value['old']
    outline = '#\t%d,%d,%f,%f\n' % (iter_no, key, new_rank, old_rank)
    sys.stdout.write(outline)
