#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

alpha = 0.85
iteration_limit = 25
iter_no = 0
n = 0 # number of nodes
graph = {} 
rank_sum = 0

for line in sys.stdin:
    key_part, value_part = line.strip().split('\t')
    value_list = value_part.split(',')
        
    if key_part == '#':
        node_i = value_list[0]
        r = float(value_list[1])
        iter_no = int(value_list[2])
        if graph.get(node_i) is None:
            graph[node_i] = {'old': 0, 'new': 0, 'neighbors': []}
        graph[node_i]['old'] = r
        rank_sum += r
        n += 1
    else:
        node_i = key_part
        new_rank = float(value_list[0])
        if graph.get(node_i) is None:
            graph[node_i] = {'old': 0, 'new': 0, 'neighbors': []}
        graph[node_i]['new'] = new_rank        
        neighbors = value_list[1:]
        for node_j in neighbors:
            if graph.get(node_j) is None:
                graph[node_j] = {'old': 0, 'new': 0, 'neighbors': []}
            graph[node_j]['neighbors'].append(node_i)

residual = (1 - alpha) / float(n) * rank_sum
for key, value in graph.iteritems():
    value['new'] = value['new'] * alpha + residual


if iter_no < iteration_limit:
    for node_i, value in graph.iteritems():
        old_rank = value['old']
        new_rank = value['new']
        outline = 'NodeId:%s:%d\t%f,%f' % (node_i, iter_no + 1, new_rank, old_rank)
        sys.stdout.write(outline)
        for node_j in value['neighbors']:
            sys.stdout.write(',%s' % node_j)
        sys.stdout.write('\n')
else:
    new_list = []
    for node, value in graph.iteritems():
        new_list.append([-value['new'], node])
    new_list.sort()
    for i in range(20):
        outline = 'FinalRank:%f\t%s\n' % (-new_list[i][0], new_list[i][1])
        sys.stdout.write(outline)
    
