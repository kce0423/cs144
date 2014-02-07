#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

graph = {}

for line in sys.stdin:
    key_part, value_part = line.split('\t')
    
    if key_part == '#':
        sys.stdout.write(line)
    else:
        node_i = int(key_part)        
        value_list = value_part.split(',')
        node_j = int(value_list[0])
        rank = float(value_list[1])
        if graph.get(node_i) is None:
            graph[node_i] = {'rank': 0, 'neighbors': []}
        graph[node_i]['rank'] += rank
        graph[node_i]['neighbors'].append(node_j)

for key, value in graph.iteritems():
    outline = '%d\t%f' % (key, value['rank'])
    sys.stdout.write(outline)
    for j in value['neighbors']:
        sys.stdout.write(',%d' % j)
    sys.stdout.write('\n')

