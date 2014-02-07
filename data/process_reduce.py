#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

iteration_limit = 50
iter_no = 0
info = {}

for line in sys.stdin:
    key_part, value_part = line.split('\t')

    if key_part == '#':
        value_list = value_part.split(',')
        iter_no = int(value_list[0])
        node_i = int(value_list[1])
        new_rank = float(value_list[2])
        old_rank = float(value_list[3])        
        if info.get(node_i) is None:
            info[node_i] = {'old': 0, 'new': 0, 'neighbors': []}
        info[node_i]['old'] = old_rank
        info[node_i]['new'] = new_rank        
    else:
        node_i = int(key_part)
        node_j = int(value_part)
        if info.get(node_i) is None:
            info[node_i] = {'old': 0, 'new': 0, 'neighbors': []}
        info[node_i]['neighbors'].append(node_j)


if iter_no < iteration_limit:
    for key, value in info.iteritems():
        old_rank = value['old']
        new_rank = value['new']
        outline = 'NodeId:%d:%d\t%f,%f' % (key, iter_no + 1, new_rank, old_rank)
        sys.stdout.write(outline)
        for j in value['neighbors']:
            sys.stdout.write(',%d' % int(j))
        sys.stdout.write('\n')
else:
    new_list = []
    for key, value in info.iteritems():
        new_list.append([-value['new'], key])
    new_list.sort()
    for i in range(20):
        outline = 'FinalRank:%f\t%d\n' % (-new_list[i][0], new_list[i][1])
        sys.stdout.write(outline)
    
